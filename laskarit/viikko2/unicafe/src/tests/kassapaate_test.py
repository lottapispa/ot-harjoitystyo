import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.saldo = Kassapaate().kassassa_rahaa
        self.edulliset = Kassapaate().edulliset
        self.maukkaat = Kassapaate().maukkaat

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.saldo), "100000")

    def test_edullisia_myyty_oikea_maara(self):
        self.assertEqual(str(self.edulliset), "0")

    def test_maukkaita_myyty_oikea_maara(self):
        self.assertEqual(str(self.maukkaat), "0")

    def test_edulliset_kateisosto_toimii(self):
        #huomaa että ostettaessa rahan määrä kasvaa kassapäätteessä
        Kassapaate().syo_edullisesti_kateisella(240)
        if self.assertNotEqual(str(Kassapaate().syo_edullisesti_kateisella(240)), 240):
            self.assertEqual(str(self.saldo), "100240")
            self.assertEqual(str(self.edulliset), "1")
        else:
            self.assertEqual(str(self.saldo), "100000")
            self.assertEqual(str(self.edulliset), "0")
    
    def test_maukkaat_kateisosto_toimii(self):
        Kassapaate().syo_maukkaasti_kateisella(400)
        if self.assertNotEqual(str(Kassapaate().syo_edullisesti_kateisella(400)), 400):
            self.assertEqual(str(self.saldo), "100400")
            self.assertEqual(str(self.maukkaat), "1")
        else:
            self.assertEqual(str(self.saldo), "100000")
            self.assertEqual(str(self.maukkaat), "0")

    #toimii tähän mennessä

    def test_edulliset_korttiosto_toimii(self):
        if self.assertTrue(Kassapaate().syo_edullisesti_kortilla(240)):
            Maksukortti().ota_rahaa(240)
            self.assertEqual(str(self.saldo), "100000")
            self.assertEqual(str(self.edulliset), "1")
            return True
        else:
            self.assertEqual(str(self.saldo), "100000")
            self.assertEqual(str(self.edulliset), "0")
            return False

    def test_maukkaat_korttiosto_toimii(self):
        if self.assertTrue(Kassapaate().syo_maukkaasti_kortilla(400)):
            Maksukortti().ota_rahaa(400)
            self.assertEqual(str(self.saldo), "100000")
            self.assertEqual(str(self.maukkaat), "1")
            return True
        else:
            self.assertEqual(str(self.saldo), "100000")
            self.assertEqual(str(self.maukkaat), "0")
            return False

    def test_rahaa_ladattaessa_kortin_saldo_muuuttuu(self):
        Kassapaate().lataa_rahaa_kortille(Maksukortti(500), 500)
        #kortin saldo muuttuu
        self.assertEqual(str(Maksukortti(500)), "Kortilla on rahaa 5.00 euroa")
        #kassassa oleva rahamäärä kasvaa
        self.assertEqual(str(self.saldo), "100000")