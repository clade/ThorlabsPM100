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
        if val[-1]=='?':
            val = val[:-1]
        out = self._record.get(val, '')
#        print('ASK', val,'...', out)
        return out

