from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import requests
import matplotlib.pyplot as plt

Base = declarative_base()


class Server(Base):
    __tablename__ = "servers"
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    register_id = Column(Integer, nullable=False, unique=True)
    server = Column(String, nullable=False)


engine = create_engine("sqlite:///server.db")
Session = sessionmaker(engine)
session = Session()


def create():
    Base.metadata.create_all(engine)


our_headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
}


def get_responses():
    for i in range(55100, 56000):
        link = f'http://register.start.bg/link.php?id={i}'
        try:
            response = requests.get(link, headers=our_headers)
        except Exception:
            continue
        else:
            if response.status_code != 200:
                continue
            server = response.headers.get('server', None)
            url = response.url
            if server is not None:
                print(server, url)
                session.add(Server(url=url, register_id=i, server=server))
                session.commit()
                # requests.post(
                #     'http://192.168.0.14:5000',
                #     data={'server': server, 'id': str(i), 'url': url})
            else:
                print(i)


def get_histogram_values():
    result = session.query(
        Server.server, func.count(Server.id)).group_by(Server.server).all()
    servers = {}
    for item in result:
        name, count = item
        name = name.lower()
        if '/' in name:
            name = name.split('/')[0]
        elif ' ' in name:
            name = name.split(' ')[1]
        c = servers.get(name, 0)
        servers[name] = count + c
    return servers


def create_histogram():
    h = get_histogram_values()
    keys = list(h.keys())
    values = list(h.values())

    X = list(range(len(keys)))

    plt.bar(X, values, align="center")
    plt.xticks(X, keys)

    plt.title(".bg servers")
    plt.xlabel("Server")
    plt.ylabel("Count")

    plt.savefig("histogram.png")


def main():
    # create()
    # get_responses()
    create_histogram()


if __name__ == '__main__':
    main()
