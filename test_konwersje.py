from konwersje import c_na_f, f_na_c


def test_zamarzanie():
    assert c_na_f(0) == 32


def test_wrzenie():
    assert f_na_c(212) == 100