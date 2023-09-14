from matplotlib import pyplot as plt

import Signal

if __name__ == '__main__':
    frequencies = [1, 2, 4, 8]
    fig, ax = plt.subplots(4, 1, layout='constrained')

    harmonic = Signal.Signal(1, Signal.SignalState.HARMONIC)
    digital = Signal.Signal(1, Signal.SignalState.DIGITAL)

    for i in range(len(frequencies)):
        harmonic.frequency = frequencies[i]
        digital.frequency = frequencies[i]
        points_of_harmonic = harmonic.create_arr_of_point_for_signal()
        points_of_digital = digital.create_arr_of_point_for_signal()
        ax[i].plot(points_of_harmonic[0], points_of_harmonic[1], color='blue', label="Гармонический")
        ax[i].plot(points_of_digital[0], points_of_digital[1], color='red', label="Цифровой")
        ax[i].set_xlabel('t')
        ax[i].set_ylabel('y')
        ax[i].set_title('Визуализация сигнала с частатой ' + str(frequencies[i]) + ' Гц')
        ax[i].legend(loc='lower left')
    plt.show()