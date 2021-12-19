"""test twitter program"""

import unittest
from mock import Mock
import buildmainfile #import main program


class TweetTest(unittest.TestCase):

    def test_example(self):
        """test funktion of main program without posting onto twitter (via Mock()"""
        mock_twitter = Mock() #instance of mock
        buildmainfile.tweet(mock_twitter, "message") #mock_twitter instead of api from twitter
        mock_twitter.PostUpdate.assert_called_with("message") #call assert_called_with method and put in expected message

    def test_example2(self):
        """another test"""
        mock_twitter = Mock()
        buildmainfile.tweet(mock_twitter, "message")
        mock_twitter.PostUpdate.assert_called_with("message")


if __name__ == '__main__':
    unittest.main()
