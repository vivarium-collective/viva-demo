from process_bigraph.emitter import emitter_from_wires, gather_emitter_results

GENE_LIST = ['maya', 'edwin', 'connor',]

def get_test_transcription_config():
    return {
        'genes': {
            'maya': {
                'transcript': 'maya',
                'rate': 0.5,
                'length': 105,
            },
            'edwin': {
                'transcript': 'edwin',
                'rate': 1.5,
                'length': 63,
            },
            'connor': {
                'transcript': 'connor',
                'rate': 1.0,
                'length': 81,
            },
        },
        "elongation_rate" : 10.0,
        "binding_rate" : 1.0,
    }

def get_test_transcription_spec():
    return {
        "_type": "process",
        "address": "local:Transcription",
        "config": get_test_transcription_config(),
        "inputs": {
            "rnap": ["RNAP"]
        },
        "outputs": {
            "rnap": ["RNAP"],
            "mrna": ["MRNA"]
        },
        "interval": 1,
    }

def get_test_simulation_spec():
    rnap = [{"free": True} for i in range(10)]
    emitter = emitter_from_wires(
        {
            "mrna": ["MRNA"],
            "rnap": ["RNAP"],
            "global_time": ["global_time"]
        }
    )
    return {
        "Transcription": get_test_transcription_spec(),
        "RNAP": rnap,
        "MRNA": {gene:0 for gene in GENE_LIST},
        "emitter": emitter,
    }
