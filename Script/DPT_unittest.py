import unittest
from unittest.mock import Mock, patch
from io import StringIO

# Importez les fonctions du script principal ici
from sonar_simulator_DPT import generate_nmea_dpt, checksum, main

class TestNMEAGenerator(unittest.TestCase):

    def test_generate_nmea_dpt(self):
        depth = 15.5
        expected_output = "$SDDPT,15.5,M*6D"
        self.assertEqual(generate_nmea_dpt(depth), expected_output)

    def test_checksum(self):
        sentence = "$SDDPT,15.5,M"
        expected_checksum = "6D"
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
            "$SDDPT,10.0,M*49\n",
            "$SDDPT,13.5,M*4E\n",
            "$SDDPT,18.0,M*57\n",
            "$SDDPT,23.0,M*66\n"
        ]
        self.assertEqual(output.getvalue(), ''.join(expected_nmea_sentences))

if __name__ == '__main__':
    unittest.main()

