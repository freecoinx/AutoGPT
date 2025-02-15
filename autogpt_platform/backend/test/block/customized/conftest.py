def pytest_addoption(parser):
   parser.addoption("--block", action="append", help="block class name") 


def pytest_generate_tests(metafunc):
   if "block" in metafunc.fixturenames:
       metafunc.parametrize("block",metafunc.config.getoption("block")) 

