from konwersje import c_na_f, f_na_c


def main():
    print("Konwerter temperatur")
    print("1 – Celsjusz → Fahrenheit")
    print("2 – Fahrenheit → Celsjusz")
    wybor = input("Wybierz opcję: ")

    try:
        wartosc = float(input("Podaj temperaturę: ").replace(",", "."))
    except ValueError:
        print("To nie jest liczba.")
        return

    if wybor == "1":
        print(f"{wartosc} °C = {c_na_f(wartosc):.1f} °F")
    elif wybor == "2":
        print(f"{wartosc} °F = {f_na_c(wartosc):.1f} °C")
    else:
        print("Nieznana opcja.")


if __name__ == "__main__":
    main()