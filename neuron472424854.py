'''
Defines a class, Neuron472424854, of neurons from Allen Brain Institute's model 472424854

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472424854:
    def __init__(self, name="Neuron472424854", x=0, y=0, z=0):
        '''Instantiate Neuron472424854.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472424854_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Rbp4-Cre_KL100_Ai14_IVSCC_-180747.02.01.01_475244723_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472424854_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 10.0
            sec.e_pas = -93.3939743042
        for sec in self.apic:
            sec.cm = 2.38
            sec.g_pas = 1.01343893064e-05
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000915010051946
        for sec in self.dend:
            sec.cm = 2.38
            sec.g_pas = 7.01296179772e-06
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.00115556
            sec.gbar_Ih = 2.29909e-05
            sec.gbar_NaTs = 1.33951
            sec.gbar_Nap = 6.1346e-05
            sec.gbar_K_P = 0.00316546
            sec.gbar_K_T = 0.00495328
            sec.gbar_SK = 0.000458406
            sec.gbar_Kv3_1 = 0.139419
            sec.gbar_Ca_HVA = 3.60557e-05
            sec.gbar_Ca_LVA = 0.00240357
            sec.gamma_CaDynamics = 0.00999901
            sec.decay_CaDynamics = 399.524
            sec.g_pas = 0.00055906
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

