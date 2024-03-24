from kalkulator import kvadrat

def main():
    test_kvadrat()

def test_kvadrat():
    if kvadrat(2) != 4:
        print("kvadrat od 2 nije 4")
    if kvadrat(3) != 9:
        print("kvadrat od 3 nije 9")
# mozemo da koristimo funkciju assert koja sluzi da pretpostavljamo nesto
    try:
      assert kvadrat(4) == 16
    except AssertionError:
        print("kvadrat od 4 nije 16")

if __name__ == "__main__":
    main()