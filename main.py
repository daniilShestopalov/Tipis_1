from matplotlib import pyplot as plt

import Signal

'''def create_draw_components(code):
    frequencies = [1, 2, 4, 8]
    if code == 1:


def onclick(event):
    if event.button == 1:'''


if __name__ == '__main__':
    frequencies = [1, 2, 4, 8]

    fig, ax = plt.subplots(4, 2, layout='constrained')

    harmonic = Signal.Signal(1, Signal.SignalState.HARMONIC)
    digital = Signal.Signal(1, Signal.SignalState.DIGITAL)


    for i in range(len(frequencies)):
        harmonic.frequency = frequencies[i]
        digital.frequency = frequencies[i]

        points_of_harmonic = harmonic.create_arr_of_point_for_signal()
        points_of_digital = digital.create_arr_of_point_for_signal()
        points_of_harmonic_spectrum = harmonic.create_arr_of_point_for_spectrum()
        points_of_digital_spectrum = digital.create_arr_of_point_for_spectrum()

        ax[i][0].plot(points_of_harmonic[0], points_of_harmonic[1], color='blue', label="Гармонический")
        ax[i][0].plot(points_of_digital[0], points_of_digital[1], color='green', label="Цифровой")
        ax[i][0].set_xlabel('Сек')
        ax[i][0].set_ylabel('В')
        ax[i][0].set_title('Визуализация сигнала с частатой ' + str(frequencies[i]) + ' Гц')
        ax[i][0].legend(loc='lower left')

        ax[i][1].plot(points_of_harmonic_spectrum[0][0], points_of_harmonic_spectrum[1][0], color='blue',
                      label="Гармонический")
        ax[i][1].plot(points_of_digital_spectrum[0][0], points_of_digital_spectrum[1][0], color='green',
                      label="Цифровой")
        ax[i][1].set_xlabel('Гц')
        ax[i][1].set_ylabel('В')
        ax[i][1].set_title('Визуализация спектра сигнала с частатой ' + str(frequencies[i]) + ' Гц')
        ax[i][1].legend(loc='lower left')
    plt.show()