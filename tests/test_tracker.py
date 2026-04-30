import unittest
from unittest.mock import patch
import requests_mock
from src.tracker import validar_ip, validar_telefono, geolocalizar_ip_metodo1, geolocalizar_ip_metodo2


class TestTracker(unittest.TestCase):
    
    def test_validar_ip_correcta(self):
        """Valida que una IP correcta sea aceptada."""
        self.assertTrue(validar_ip("1.1.1.1"))
        self.assertTrue(validar_ip("192.168.1.1"))
        self.assertTrue(validar_ip("255.255.255.255"))

    def test_validar_ip_incorrecta(self):
        """Valida que IPs incorrectas sean rechazadas."""
        self.assertFalse(validar_ip("256.256.256.256"))
        self.assertFalse(validar_ip("1.2.3"))
        self.assertFalse(validar_ip("abc.def.ghi.jkl"))

    def test_validar_telefono_correcto(self):
        """Valida que un número de teléfono correcto sea aceptado."""
        # Nota: requiere el formato correcto (+ código)
        self.assertTrue(validar_telefono("+14155552671"))

    def test_validar_telefono_incorrecto(self):
        """Valida que un número de teléfono incorrecto sea rechazado."""
        self.assertFalse(validar_telefono("12345"))
        self.assertFalse(validar_telefono("+0000000000"))

    @requests_mock.Mocker()
    def test_geolocalizar_ip_metodo1_success(self, m):
        """Prueba éxito del método 1 con mock."""
        mock_response = {
            "status": "success",
            "query": "1.1.1.1",
            "country": "Australia",
            "countryCode": "AU",
            "regionName": "Queensland",
            "city": "South Brisbane",
            "zip": "4101",
            "lat": -27.4766,
            "lon": 153.0166,
            "timezone": "Australia/Brisbane",
            "isp": "Cloudflare, Inc.",
            "org": "APNIC-AS-BLOCK",
            "as": "AS13335 Cloudflare, Inc."
        }
        m.get('http://ip-api.com/json/1.1.1.1', json=mock_response)
        
        # Usamos patch para evitar que intente crear carpetas o imprimir en el test
        with patch('src.tracker.crear_carpeta_resultados', return_value="test_results"):
            with patch('builtins.open', unittest.mock.mock_open()):
                result = geolocalizar_ip_metodo1("1.1.1.1")
                self.assertIsNotNone(result)
                self.assertEqual(result['country'], "Australia")

    @requests_mock.Mocker()
    def test_geolocalizar_ip_metodo2_success(self, m):
        """Prueba éxito del método 2 con mock."""
        mock_response = {
            "ip": "8.8.8.8",
            "city": "Mountain View",
            "region": "California",
            "country": "US",
            "loc": "37.4056,-122.0775",
            "org": "AS15169 Google LLC",
            "postal": "94043",
            "timezone": "America/Los_Angeles"
        }
        m.get('https://ipinfo.io/8.8.8.8/json', json=mock_response)
        
        with patch('src.tracker.crear_carpeta_resultados', return_value="test_results"):
            with patch('builtins.open', unittest.mock.mock_open()):
                result = geolocalizar_ip_metodo2("8.8.8.8")
                self.assertIsNotNone(result)
                self.assertEqual(result['city'], "Mountain View")


if __name__ == '__main__':
    unittest.main()

