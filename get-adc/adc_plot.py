import matplotlib.pyplot as plt


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))

    plt.plot(time, voltage)

    plt.title("График зависимости напряжения на входе АЦП от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    
    plt.axis([min(time), max(time), 0, max_voltage])

    plt.minorticks_on()
    plt.grid(visible=True, which='major')
    plt.grid(visible=True, which='minor')

    plt.show()