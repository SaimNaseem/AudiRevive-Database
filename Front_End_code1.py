import time

# Geschwindigkeit 1
def print_text_slowly0(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Geschwindigkeit 2
def print_text_slowly1(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()





# Example usage:
if __name__ == "__main__":
    print_text_slowly0("SAEM AI\n")

    print_text_slowly1("Hir konnen Sie alle Audi Jahreswagen Modelle suchen")
    


#
#
import pandas as pd

# Funktion zum Einlesen der Daten aus Excel
def read_data_from_excel(file_path, sheet_name):
    try:
        # Annahme: Die Daten befinden sich in der Tabelle ab der ersten Zeile (Header)
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        return df
    except Exception as e:
        print(f"Fehler beim Einlesen der Daten: {e}")
        return None

# Funktion für Benutzereingabe
def get_user_input():
    user_sheet_input = input("Bitte geben Sie den Namen des Sheets ein (A1, A3, A4, A5 , A6): ")
    user_data_input = input("Bitte geben Sie Ihre Eingabe ein: ")
    return user_sheet_input, user_data_input

# Beispielanwendung:
if __name__ == "__main__":
    # Ersetzen Sie 'Pfad_zur_Ihrer_Datei.xlsx' durch den tatsächlichen Pfad zu Ihrer Excel-Datei
    file_path0 = "A_Modelle.xlsx"

    # Setzen Sie Pandas-Optionen, um alle Spalten und Zeilen anzuzeigen
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Benutzereingabe abfragen
    sheet_name, user_input = get_user_input()

    # Daten aus Excel einlesen basierend auf der Benutzereingabe
    data_frame = read_data_from_excel(file_path0, sheet_name)

    if data_frame is not None:
        # Anzeige der Daten (optional)
        print(data_frame)

        # Hier können Sie den Benutzereingabe und das ausgewählte Sheet weiter verarbeiten
        print(f"Sie haben das Sheet '{sheet_name}' ausgewählt.")
        print(f"Ihre Eingabe lautet: {user_input}")
input("::")