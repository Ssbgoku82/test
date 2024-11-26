import unittest
from television import Television

class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv = Television()

    def test_initial_state(self):
        self.assertFalse(self.tv._Television__status)
        self.assertFalse(self.tv._Television__muted)
        self.assertEqual(self.tv._Television__volume, Television.MIN_VOLUME)
        self.assertEqual(self.tv._Television__channel, Television.MIN_CHANNEL)

    def test_power(self):
        self.tv.power()
        self.assertTrue(self.tv._Television__status)
        self.tv.power()
        self.assertFalse(self.tv._Television__status)

    def test_mute(self):
        self.tv.power()  # Turn TV on
        self.tv.mute()   # Mute the TV
        self.assertTrue(self.tv._Television__muted)
        self.assertEqual(self.tv._Television__volume, 0)

        self.tv.mute()   # Unmute the TV
        self.assertFalse(self.tv._Television__muted)

    def test_channel_up(self):
        self.tv.power()  # Turn TV on
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, 1)
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()  # Wrap around to MIN_CHANNEL
        self.assertEqual(self.tv._Television__channel, Television.MIN_CHANNEL)

    def test_channel_down(self):
        self.tv.power()  # Turn TV on
        self.tv.channel_down()  # Wrap around to MAX_CHANNEL
        self.assertEqual(self.tv._Television__channel, Television.MAX_CHANNEL)

    def test_volume_up(self):
        self.tv.power()  # Turn TV on
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, 1)
        self.tv.volume_up()
        self.tv.volume_up()  # Max volume
        self.assertEqual(self.tv._Television__volume, Television.MAX_VOLUME)
        self.tv.volume_up()  # Should stay at MAX_VOLUME
        self.assertEqual(self.tv._Television__volume, Television.MAX_VOLUME)

    def test_volume_down(self):
        self.tv.power()  # Turn TV on
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, 1)
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, Television.MIN_VOLUME)
        self.tv.volume_down()  # Should stay at MIN_VOLUME
        self.assertEqual(self.tv._Television__volume, Television.MIN_VOLUME)

    def test_str(self):
        self.tv.power()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")
        self.tv.volume_up()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 1")
        self.tv.mute()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 1")

if __name__ == '__main__':
    unittest.main()
