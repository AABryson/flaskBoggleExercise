from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class ViewFunctions(TestCase):
    def test_root_page(self):
        with app.text_client() as client:
            response=client.get('/')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('gameboard', session)
            self.assertNone(session.get('highscore'))
            self.assertNone(session.get('nplays'))
            self.assertIn('<h3>High Score', response.data)


    def test_handle_guess(self):
        with app.text_client() as client:
            response = client.get('/handle_guess')
            self.assertEqual(response.status_code, 200)
            self.assertIn('gameBoard', session)
            with app.test_request_context('/handle_guess'):
                self.assertIn('inputValue', request.args)


    def test_game_over(self):
        with app.text_client() as client:
            response=client.get('/gameover')
            html = response.get_data(as_text=True)
            self.assertIn('score', response)

 

