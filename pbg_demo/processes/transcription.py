from process_bigraph import Process
import random

gene = {
    'transcript' : 'string', # Transcript name
    'rate' : 'float', # binding probability for each gene
    'length' : 'integer', # number of nucleotides
}

rnap = {
    'free' : 'boolean', # bound or not
    'gene' : 'string', # name of the gene
    'position' : 'integer', # nucleotide position
}

class Transcription(Process):
    config_schema = {
        'genes': 'map[gene]', # map of genes to transcripts
        'elongation_rate': 'float', # global RNAP elongation rate
        'binding_rate': 'float', # global RNAP binding rate
    }

    def initialize(self):
        self.genes = self.config['genes']
        self.elongation_rate = self.config['elongation_rate']
        self.total_rate = sum([gene['rate'] for gene in self.genes.values()])
        self.binding_rate = self.config['binding_rate']

    def select_gene(self):
        """
        This function selects a gene for RNAP binding based on binding rates.
        """
        choice = random.random() * self.total_rate

        for key,gene in self.genes.items():
            if choice < gene['rate']:
                break
            else:
                choice -= gene['rate']
        return key


    def inputs(self):
        return {
            'rnap': 'list[rnap]',
        }

    def output(self):
        return {
            'rnap' : 'list[rnap]',
            'mRNA' : 'map[integer]',
        }

    def update(self, state, interval):
        # Separate free and bound RNAPs
        free_rnap = [rnap for rnap in state['rnap'] if rnap['free']]
        bound_rnap = [rnap for rnap in state['rnap'] if not rnap['free']]

        mRNA = {}
        rnap = []

        # Calculate elongation length
        elongation = int(self.elongation_rate * interval)

        # Loop through all the bound RNAPs and update position by elongation length or
        # Add completed transcripts to the mRNA dictionary and set RNAP free
        for bound in bound_rnap:
            gene = self.genes[bound['gene']]
            gene_length = gene['length']
            elongate_to = bound['position'] + elongation
            if elongate_to >= gene_length:
                transcript = gene['transcript']
                if transcript not in mRNA:
                    mRNA[transcript] = 0
                mRNA[transcript] += 1
                rnap.append({'free': True})

            else:
                bound = bound.copy()
                bound['position'] = elongate_to
                rnap.append(bound)

        free_count = len(free_rnap)

        # Calculate the binding events
        binding_count = self.binding_rate * free_count * interval

        # Update free RNAPs
        for free in range(free_count - binding_count):
            rnap.append({'free': True})

        # Update bound RNAPs
        for binding in range(binding_count):
            gene_key = self.select_gene()
            rnap.append({'free': False, 'gene': gene_key, 'position': 0})

        return {
            'rnap': rnap,
            'mRNA': mRNA,
        }






