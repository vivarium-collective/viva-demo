from pprint import pprint

from pbg_demo import register_types
from pbg_demo.processes import Transcription, register_processes
from pbg_demo.utils.utils import get_test_simulation_spec
from process_bigraph import allocate_core, Composite
from process_bigraph.emitter import gather_emitter_results

def run_test_simulation(core):
    spec = get_test_simulation_spec()
    sim = Composite(
        {"state":spec},
        core,
    )

    sim.run(50)
    results = gather_emitter_results(sim)[('emitter',)]
    return results

if __name__ == "__main__":
    core = allocate_core()
    register_types(core)
    register_processes(core)
    results = run_test_simulation(core)
    pprint(results)