from matplotlib import pyplot as plt

import Signal

fig, ax = plt.subplots(4, 1, layout='constrained')
def create_draw_components(code):
    frequencies = [1, 2, 4, 8]

    harmonic = Signal.Signal(1, Signal.SignalState.HARMONIC)
    digital = Signal.Signal(1, Signal.SignalState.DIGITAL)
    points = []

    for i in range(len(frequencies)):
        ax[i].cla()
        harmonic.frequency = frequencies[i]
        digital.frequency = frequencies[i]
        if code == 1 or code == 2:
            if code == 1:
                points = harmonic.create_arr_of_point_for_signal()
                ax[i].plot(points[0], points[1], color='blue', label="Гармонический")
            elif code == 2:
                points = digital.create_arr_of_point_for_signal()
                ax[i].plot(points[0], points[1], color='red', label="Цифровой")
            ax[i].set_xlabel('Сек')
            ax[i].set_ylabel('В')
            ax[i].set_title('Визуализация сигнала с частатой ' + str(frequencies[i]) + ' Гц')
            ax[i].legend(loc='lower left')
        elif code == 3 or code == 4:
            if code == 3:
                points = harmonic.create_arr_of_point_for_spectrum()
                ax[i].plot(points[0][0], points[1][0], color='blue',
                              label="Гармонический")
            elif code == 4:
                points = digital.create_arr_of_point_for_spectrum()
                ax[i].plot(points[0][0], points[1][0], color='red', label="Цифровой")
            ax[i].set_xlabel('Гц')
            ax[i].set_ylabel('В')
            ax[i].set_title('Визуализация спектра сигнала с частатой ' + str(frequencies[i]) + ' Гц')
            ax[i].legend(loc='lower left')
    plt.draw()
    plt.pause(0.5)

def onclick(event):
    global index
    if event.button == 3:
        index += 1
        if index > 4:
            index = 1
        create_draw_components(index)


if __name__ == '__main__':
    global index
    index = 1
    create_draw_components(index)
    plt.connect('button_press_event', onclick)
    plt.show()
