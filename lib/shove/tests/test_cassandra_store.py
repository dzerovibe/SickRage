# -*- coding: utf-8 -*-

import unittest


class TestCassandraStore(unittest.TestCase):

    def setUp(self):
        from shove import Shove
        from pycassa.system_manager import SystemManager
        system_manager = SystemManager('localhost:9160')
        try:
            system_manager.create_column_family('Foo', 'shove')
        except:
            pass
        self.store = Shove('cassandra://localhost:9160/Foo/shove')

    def tearDown(self):
        self.store.clear()
        self.store.close()
        from pycassa.system_manager import SystemManager
        system_manager = SystemManager('localhost:9160')
        system_manager.drop_column_family('Foo', 'shove')

    def test__getitem__(self):
        self.store['max'] = 3
        self.assertEqual(self.store['max'], 3)

    def test__setitem__(self):
        self.store['max'] = 3
        self.assertEqual(self.store['max'], 3)

    def test__delitem__(self):
        self.store['max'] = 3
        del self.store['max']
        self.assertEqual('max' in self.store, False)

    def test_get(self):
        self.store['max'] = 3
        self.assertEqual(self.store.get('min'), None)

    def test__cmp__(self):
        from shove import Shove
        tstore = Shove()
        self.store['max'] = 3
        tstore['max'] = 3
        self.assertEqual(self.store, tstore)

    def test__len__(self):
        self.store['max'] = 3
        self.store['min'] = 6
        self.assertEqual(len(self.store), 2)

#    def test_clear(self):
#        self.store['max'] = 3
#        self.store['min'] = 6
#        self.store['pow'] = 7
#        self.store.clear()
#        self.assertEqual(len(self.store), 0)

    def test_items(self):
        self.store['max'] = 3
        self.store['min'] = 6
        self.store['pow'] = 7
        slist = list(self.store.items())
        self.assertEqual(('min', 6) in slist, True)

    def test_iteritems(self):
        self.store['max'] = 3
        self.store['min'] = 6
        self.store['pow'] = 7
        slist = list(self.store.iteritems())
        self.assertEqual(('min', 6) in slist, True)

    def test_iterkeys(self):
        self.store['max'] = 3
        self.store['min'] = 6
        self.store['pow'] = 7
        slist = list(self.store.iterkeys())
        self.assertEqual('min' in slist, True)

    def test_itervalues(self):
        self.store['max'] = 3
        self.store['min'] = 6
        self.store['pow'] = 7
        slist = list(self.store.itervalues())
        self.assertEqual(6 in slist, True)

    def test_pop(self):
        self.store['max'] = 3
        self.store['min'] = 6
        item = self.store.pop('min')
        self.assertEqual(item, 6)

#    def test_popitem(self):
#        self.store['max'] = 3
#        self.store['min'] = 6
#        self.store['pow'] = 7
#        item = self.store.popitem()
#        self.assertEqual(len(item) + len(self.store), 4)

    def test_setdefault(self):
        self.store['max'] = 3
        self.store['min'] = 6
#        self.store['pow'] = 7
        self.store.setdefault('pow', 8)
        self.assertEqual(self.store.setdefault('pow', 8), 8)
        self.assertEqual(self.store['pow'], 8)

    def test_update(self):
        from shove import Shove
        tstore = Shove()
        tstore['max'] = 3
        tstore['min'] = 6
        tstore['pow'] = 7
        self.store['max'] = 2
        self.store['min'] = 3
        self.store['pow'] = 7
        self.store.update(tstore)
        self.assertEqual(self.store['min'], 6)

    def test_values(self):
        self.store['max'] = 3
        self.store['min'] = 6
        self.store['pow'] = 7
        slist = self.store.values()
        self.assertEqual(6 in slist, True)

    def test_keys(self):
        self.store['max'] = 3
        self.store['min'] = 6
        self.store['pow'] = 7
        slist = self.store.keys()
        self.assertEqual('min' in slist, True)

if __name__ == '__main__':
    unittest.main()
