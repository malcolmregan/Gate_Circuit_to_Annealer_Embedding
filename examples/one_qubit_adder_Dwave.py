import dimod
from dwave.system.samplers import DWaveSampler
from dwave.cloud.exceptions import SolverOfflineError
from dwave.system.composites import EmbeddingComposite

token = ''
numofsamples = 400

qubit_biases = {397: 5,
                393: 10,
                398: 5,
                394: 10,
                396: 9,
                399: 8,
                392: 13,
                395: 9,
                264: 10,
                136: 9,
                266: 10,
                138: 10,
                142: 10,
                137: 5,
                141: 10,
                139: 8,
                140: 13,
                143: 9,
                148: 10,
                156: 9,
                149: 10,
                157: 10,
                521: 10,
                525: 10,
                533: 10,
                529: 10,
                401: 10,
                273: 10,
                145: 10,
                151: 10,
                159: 10,
                153: 10,
                155: 10,
                158: 8,
                152: 8,
                154: 9,
                283: 10,
                411: 11,
                415: 6,
                409: 6,
                413: 6,
                408: 9,
                412: 9,
                421: 10,
                429: 6,
                134: 10,
                130: 10,
                2: 10,
                6: 10,
                14: 10,
                22: 10,
                30: 10,
                38: 10,
                34: 10,
                162: 10,
                290: 10,
                418: 10,
                422: 10,
                430: 11,
                426: 6,
                425: 6,
                428: 9,
                424: 9,
                297: 10,
                169: 6,
                25: 10,
                29: 10,
                37: 10,
                33: 10,
                161: 10,
                289: 10,
                293: 10,
                301: 10,
                299: 10,
                171: 11,
                175: 6,
                173: 1,
                168: 9,
                172: 9}

coupler_strengths = {(393, 397): -10,
                     (394, 398): -10,
                     (392, 399): -13,
                     (395, 396): -9,
                     (395, 397): -4,
                     (395, 398): -5,
                     (395, 399): 9,
                     (392, 396): -7,
                     (393, 399): -2,
                     (394, 399): -2,
                     (393, 396): 2,
                     (394, 396): 2,
                     (394, 397): 1,
                     (264, 392): -10,
                     (136, 264): -10,
                     (266, 394): -10,
                     (138, 266): -10,
                     (138, 142): -10,
                     (137, 141): -10,
                     (139, 140): -13,
                     (136, 143): -9,
                     (138, 143): -4,
                     (137, 143): -5,
                     (139, 143): 9,
                     (136, 140): -7,
                     (139, 142): -2,
                     (139, 141): -2,
                     (136, 142): 2,
                     (136, 141): 2,
                     (138, 141): 1,
                     (140, 148): -10,
                     (148, 156): -10,
                     (141, 149): -10,
                     (149, 157): -10,
                     (393, 521): -10,
                     (521, 525): -10,
                     (525, 533): -10,
                     (529, 533): -10,
                     (401, 529): -10,
                     (273, 401): -10,
                     (145, 273): -10,
                     (145, 151): -10,
                     (151, 159): -10,
                     (153, 157): -10,
                     (155, 159): -10,
                     (152, 158): -13,
                     (154, 156): -9,
                     (154, 157): -4,
                     (154, 159): -5,
                     (154, 158): 9,
                     (152, 156): -7,
                     (153, 158): -2,
                     (155, 158): -2,
                     (153, 156): 2,
                     (155, 156): 2,
                     (155, 157): 1,
                     (155, 283): -10,
                     (283, 411): -10,
                     (408, 412): -14,
                     (408, 415): -4,
                     (409, 412): -4,
                     (408, 413): 4,
                     (411, 415): -11,
                     (411, 413): -2,
                     (409, 415): 2,
                     (409, 413): -2,
                     (413, 421): -10,
                     (421, 429): -10,
                     (134, 142): -10,
                     (130, 134): -10,
                     (2, 130): -10,
                     (2, 6): -10,
                     (6, 14): -10,
                     (14, 22): -10,
                     (22, 30): -10,
                     (30, 38): -10,
                     (34, 38): -10,
                     (34, 162): -10,
                     (162, 290): -10,
                     (290, 418): -10,
                     (418, 422): -10,
                     (422, 430): -10,
                     (424, 428): -14,
                     (426, 428): -4,
                     (424, 429): -4,
                     (425, 428): 4,
                     (426, 430): -11,
                     (425, 430): -2,
                     (426, 429): 2,
                     (425, 429): -2,
                     (297, 425): -10,
                     (169, 297): -10,
                     (25, 153): -10,
                     (25, 29): -10,
                     (29, 37): -10,
                     (33, 37): -10,
                     (33, 161): -10,
                     (161, 289): -10,
                     (289, 293): -10,
                     (293, 301): -10,
                     (299, 301): -10,
                     (171, 299): -10,
                     (168, 172): -14,
                     (168, 175): -4,
                     (169, 172): -4,
                     (168, 173): 4,
                     (171, 175): -11,
                     (171, 173): -2,
                     (169, 175): 2,
                     (169, 173): -2}

inputs = [397, 398, 137]
outputs = [173, 152]

sampler = DWaveSampler(endpoint='https://cloud.dwavesys.com/sapi', token = token, solver = 'DW_2000Q_2_1')

bqm = dimod.BinaryQuadraticModel(qubit_biases, coupler_strengths, 0, dimod.BINARY)

kwargs = {}
if 'num_reads' in sampler.parameters:
   kwargs['num_reads'] = numofsamples
if 'answer_mode' in sampler.parameters:
   kwargs['answer_mode'] = 'histogram'
#if 'annealing_time' in sampler.parameters:
#    kwargs['annealing_time'] = 100
print('\nRunning...')

response = sampler.sample(bqm, **kwargs)

sampler.client.close()
print('Done.')
print(response.data)

groundstate = 1000000
for sample, energy in response.data(['sample','energy']):
   if energy<groundstate:
       groundstate = round(energy,1)
print('Ground State: ', groundstate)

function = list()
for sample, energy in response.data(['sample', 'energy']):
   if round(energy,1) == groundstate:
       print(sample, round(energy,1))
       row = []
       for inp in inputs:
           row.append(sample[inp])
       for outp in outputs:
           row.append(sample[outp])
       function.append(row)
print('\n')

function.sort()
for i in range(len(function)):
   print(function[i])
