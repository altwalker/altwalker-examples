import sys
import pdb

# It's important to initalize the debuger with the sys.stdout as output because durring the execution of
# the tests methods altwalker will redirect the output using ``contextlib.redirect_output``.
debugger = pdb.Pdb(skip=['altwalker.*'], stdout=sys.stdout)


class DebugModel:

    def v_state_a(self):
        pass

    def v_state_b(self):
        pass

    def v_state_c(self):
        debugger.set_trace()

    def e_action_a(self):
        pass

    def e_action_b(self):
        pass

    def e_action_c(self):
        pass
