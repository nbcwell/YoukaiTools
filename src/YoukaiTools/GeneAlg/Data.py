from . import SelectionTypes

def make_report(top_object, top_fitness, generation, termination_generation, time, termination_time):
    d = {}
    d["top_object"] = top_object
    d["top_fitness"] = top_fitness
    d["generation"] = generation
    d["termination_generation"] = termination_generation
    d["time"] = time
    d["termination_time"] = termination_time
    return d

def make_gene(fitness, mate, mutate, generate, report=lambda (obj,fitness,generation,topgeneration):1):
    d = {}
    d["fitness"] = fitness
    d["mate"] = mate
    d["mutate"] = mutate
    d["report"] = report
    d["generate"] = generate
    return d
        
def make_options(selection=SelectionTypes.tourney_select, selection_settings=(2,), deletion=SelectionTypes.tourney_low_select, deletion_settings=(2,), mc=.5, mimin=0, mimax=1.0, seeds = None):
    d = {}
    d["selection"] = selection
    d["selection_settings"] = selection_settings
    d["deletion"] = deletion
    d["deletion_settings"] = deletion_settings
    d["mutation_chance"] = mc
    d["mutation_intensity_min"] = mimin
    d["mutation_intensity_max"] = mimax
    d["seeds"] = seeds
    return d

def make_criteria(time=None, generations=None):
    d = {}
    d["time"] = time
    d["generations"] = generations
    return d
