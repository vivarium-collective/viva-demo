from pbg_demo.processes.transcription import Transcription

def register_processes(core):
    core.register_link("Transcription", Transcription)
    return core