import argparse
import logging

from pyfeedstg.server import Server


if __name__ == '__main__':
    appDescription = 'Forwarding articles from RSS/Atom feeds to Telegram'

    parser = argparse.ArgumentParser(description=appDescription)
    parser.add_argument('-c', '--config',
                        default='/Users/ilyautekhin/Downloads/pyFeedsTgBot-master\ 3/bot/config.yml',
                        help='Choose file with bot\'s configuration')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Switch logging to DEBUG')
    parser.add_argument('-l', '--latest', action='store_true',
                        help='Immediatly send latest entry in feed')
    args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(message)s')
    logger = logging.getLogger()

    if args.debug:
        logger.setLevel(level=logging.DEBUG)
    else:
        logger.setLevel(level=logging.INFO)

    logging.info('Start server with "{}" configuration'.format(args.config))

    try:
        Server(filename=args.config, sendLatestEntry=args.latest).run()
    except:
        raise
