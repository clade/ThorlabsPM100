class FakeSCPI(object):
    _record = {}
    def write(self, val):
#        print('WRITE', val)
        if ' ' in val:
            cmd, vals = val.split(' ')
            self._record[cmd] = vals
        else:
            self._record[val] = True

    def query(self, val):
        assert val[-1]=='?'
        out = self._record.get(val[:-1], '')
#        print('ASK', val,'...', out)
        return out

