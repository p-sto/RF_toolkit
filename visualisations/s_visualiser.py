""""""
import os
from typing import Dict, List, Optional, Tuple

from scikit_rf_ext.LTEBands import FrequencySpan

try:
    import skrf as rf
except ImportError:
    raise ImportError('Please install scikit-rf')

try:
    import matplotlib.pyplot as plt
    import matplotlib.transforms as transforms
except ImportError:
    raise ImportError('Please install scikit-rf')


_frequencies_map = {
    'khz': 1e3,
    'mhz': 1e6,
    'ghz': 1e9
}


def map_s_params(params: str) -> Dict:
    """Accepts S-param in format 'S21' and maps it to scikitrf format"""
    params = params.lower()
    assert params.startswith('s')
    assert len(params) == 3
    params = params[1:]
    try:
        return {
            'm': int(params[0]) - 1,
            'n': int(params[1]) - 1
        }
    except Exception as err:
        print(err)


class Analyser:

    _default_freq_format = 'ghz'
    _default_colors = [
        'tab:blue',
        'tab:green',
        'tab:orange',
        'tab:purple'
    ]

    def __init__(
            self,
            networks: rf.Network | List[rf.Network],
            output_dir: str = os.path.curdir,
            freq_format: Optional[str] = None
    ):
        self.networks = networks if isinstance(networks, list) else [networks]
        self.output_dir = output_dir

        if len(self.networks) > 4:
            raise AttributeError('Cannot fit more than 4 networks in one graph.')       # no colors!

        _freq_format = freq_format or self._default_freq_format

        for ntwrk in self.networks:
            ntwrk.frequency.unit = _freq_format

    @staticmethod
    def __mark_frequencies(mark_frequencies: str | FrequencySpan, marked_label: Optional[str]):
        if isinstance(mark_frequencies, str):
            for _freq, multiplier in _frequencies_map.items():
                if _freq in mark_frequencies.lower():
                    _min = float(mark_frequencies.lower().split('-')[0].strip(_freq)) * multiplier
                    _max = float(mark_frequencies.lower().split('-')[1].strip(_freq)) * multiplier
                    plt.axvspan(_min, _max, color='tab:grey', alpha=0.2)
                    break
        else:
            assert isinstance(mark_frequencies, FrequencySpan), "mark_frequencies is not Tuple"
            _min = mark_frequencies.start * _frequencies_map['mhz']
            _max = mark_frequencies.stop * _frequencies_map['mhz']

            if marked_label:
                plt.axvspan(_min, _max, color='tab:blue', alpha=0.2, label=marked_label)
            else:
                plt.axvspan(_min, _max, color='tab:blue', alpha=0.2)

    def __calc_avg_min_gain_freq(self, mark_frequencies: str | FrequencySpan, ax: plt.Axes):
        _networks = []

        if isinstance(mark_frequencies, str):
            pass
        else:
            assert isinstance(mark_frequencies, FrequencySpan), "mark_frequencies is not Tuple"
            for ntwrk in self.networks:
                _networks.append(ntwrk['{}MHz-{}MHz'.format(mark_frequencies.start, mark_frequencies.stop)])

        for ntwrk, color in zip(_networks, self._default_colors):
            ntwrk.frequency.unit = self._default_freq_format
            values = [p.s_db.item() for p in ntwrk.s21]
            avg = sum(values) / len(values)

            trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
            ax.text(1.12, avg, "avg:\n{:.2f}".format(avg), color=color, transform=trans, ha="right", va="center")

            plt.axhline(y=avg, color=color, linestyle='--')
            print(
                'Average gain [{}] for frequency span [{}]'.format(
                    avg, '{}-{}'.format(ntwrk.frequency.start, ntwrk.frequency.stop)
                )
            )
            _min = min(values)
            print(
                'Min gain [{}] for frequency span [{}]'.format(
                    _min, '{}-{}'.format(ntwrk.frequency.start, ntwrk.frequency.stop))
            )

    def gen_s_visualisation(
            self,
            s_params: List[str],
            strip_frequency: Optional[Tuple[float, float]] = None,
            mark_frequencies: Optional[str | FrequencySpan] = None,
            marked_label: Optional[str] = None,
            calc_avg_gain_freq: bool = False

    ) -> None:
        """"""

        for s_param in s_params:
            for ntwrk, color in zip(self.networks, self._default_colors):
                plt.clf()  # cleans plt
                ax = plt.gca()
                ax.set_title('|{}| Param'.format(s_param), y=1.05)
                ax.grid(visible=True)

                if strip_frequency:
                    _start, _stop = strip_frequency
                    ntwrk = ntwrk['{}MHz-{}MHz'.format(_start, _stop)]

                if mark_frequencies:
                    self.__mark_frequencies(mark_frequencies, marked_label)
                    if calc_avg_gain_freq:
                        self.__calc_avg_min_gain_freq(mark_frequencies, ax)

                ntwrk.plot_s_db(**map_s_params(s_param), ax=ax, color=color)

                if not os.path.exists(self.output_dir):
                    os.makedirs(self.output_dir)

                ax.legend(loc='lower center', facecolor='white', framealpha=1)
                plt.savefig('{}/{}_{}.png'.format(self.output_dir, ntwrk.name, s_param), dpi=600)
