import unittest
from unittest.mock import Mock, patch
from io import StringIO

# Importez les fonctions du script principal ici
from sonar_simulator_DPT import generate_nmea_dpt, checksum, main

class TestNMEAGenerator(unittest.TestCase):

    def test_generate_nmea_dpt(self):
        depth = 15.5
        expected_output = "$SDDPT,15.5,0.1,100*7A"
        self.assertEqual(generate_nmea_dpt(depth), expected_output)

    def test_checksum(self):
        sentence = "SDDPT,15.5,0.1,100"
        expected_checksum = "7A"
        self.assertEqual(checksum(sentence), expected_checksum)

    @patch('serial.Serial')
    @patch('time.time', side_effect=[0, 1, 2, 3])  # Pour contrôler le temps dans les tests
    def test_main(self, mock_time, mock_serial):
        # Créez un faux objet Serial pour les tests
        mock_ser = Mock()
        mock_serial.return_value = mock_ser

        # Utilisez un StringIO pour capturer la sortie imprimée
        output = StringIO()
        with patch('sys.argv', ['script_principal.py', 'test_port_serie', '9600']), \
             patch('sys.stdout', output):
            main('test_port_serie', 9600)

        # Vérifiez que la fonction Serial a été appelée avec les bons arguments
        mock_serial.assert_called_once_with('test_port_serie', 9600, timeout=1)
        # Vérifiez que la phrase NMEA a été correctement générée et envoyée
        expected_nmea_sentences = [
            "$SDDPT,10.0,0.1,100*7A",
            "$SDDPT,20.0,0.1,100*79",
            "$SDDPT,30.0,0.1,100*78",
            "$SDDPT,40.0,0.1,100*7F"
        ]
        self.assertEqual(output.getvalue(), ''.join(expected_nmea_sentences))

if __name__ == '__main__':
    unittest.main()

