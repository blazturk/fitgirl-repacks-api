from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

def get_magnet(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  page_link = soup.find_all('a', string='magnet')

  return page_link[0].get('href')

def get_torrent(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  page_link = soup.find_all(string='.torrent file only', attrs={"rel": "noopener"})

  return page_link[0].get('href')

app = Flask(__name__)



@app.route('/torrent', methods=['GET'])
def get_link():
 return jsonify(links)

@app.route('/torrent/<path:link>', methods=['GET'])
def get_torrent_link_by_url(link):
    decoded_url = 'https://' + link
    page_link = get_torrent(decoded_url)

    if page_link is None:
        return jsonify({'error': 'No links available'}), 404

    return jsonify({'torrent': page_link})


@app.route('/magnet/<path:link>', methods=['GET'])
def get_magnet_link_by_url(link):
    decoded_url = 'https://' + link
    page_link = get_magnet(decoded_url)

    if page_link is None:
        return jsonify({'error': 'No links available'}), 404

    return jsonify({'magnet': page_link})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)




