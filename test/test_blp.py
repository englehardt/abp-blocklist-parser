from abp_blocklist_parser.BlockListParser import BlockListParser
import requests
import pytest



@pytest.fixture(scope="module")
def block_list_parser():
    # Download blocklists
    raw_lists = {
    'nocoin': 'https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt',
    'ublock-resource-abuse': 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt'
    }
    # Initialize parsers
    blockers = [
    BlockListParser(regexes=requests.get(raw_lists["nocoin"]).content.decode()),
    BlockListParser(regexes=requests.get(raw_lists["ublock-resource-abuse"]).content.decode())
    ]
    return blockers[0]


def test_should_block(block_list_parser: BlockListParser) -> None:
    should_block_my_domain = block_list_parser.should_block("https://zabka.it")
    assert not should_block_my_domain

def test_should_block_and_print(block_list_parser: BlockListParser)-> None:
    should_block_my_domain = block_list_parser.should_block_and_print("https://zabka.it")
    assert not should_block_my_domain

def test_should_block_with_items(block_list_parser: BlockListParser)-> None:
    should_block_my_domain = block_list_parser.should_block_with_items("https://zabka.it")
    assert not should_block_my_domain

