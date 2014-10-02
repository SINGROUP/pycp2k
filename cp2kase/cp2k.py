#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""This module defines an ASE calculator interface to CP2K."""

from cp2kase.parsedclasses import CP2K_INPUT1
from ase.calculators.interface import Calculator
from subprocess import call


#===============================================================================
class CP2K(Calculator):
    """Class for doing CP2K calculations.

    This class is an ASE compatible calculator interface for CP2K. You use it
    to create an input file for CP2K in a pythonic object-oriented way. The
    advantages of this are:
        -Access to ASE's structure creation tools
        -ASE input/output
        -Script multiple runs with python
        -Automatic syntax correctness for the input file
        -Code completion if provided by your python IDE

    Attributes:

    """
    def __init__(self, input_path=None, output_path=None):
        """Construct CP2K-calculator object."""
        self.CP2K_INPUT = CP2K_INPUT1()
        self.input_path = input_path
        self.output_path = output_path
        self.cp2k_command = "cp2k"
        self.cp2k_flags = {}
        self.mpi_on = True
        self.mpi_flags = {}
        self.mpi_n_processes = None
        self.mpi_command = "mpirun"

    def __del__(self):
        """Destructor"""

    def set_input_path(self, input_path):
        """Set the path where all the input an."""
        self.input_path = input_path

    def set_output_path(self, output_path):
        """Set the path where all the input an."""
        self.output_path = output_path

    def calculation_required(atoms, quantities):
        """Check if a calculation is required.

        Check if the quantities in the quantities list have already been calculated
        for the atomic configuration atoms. The quantities can be one or more of:
        ‘energy’, ‘forces’, ‘stress’, ‘charges’ and ‘magmoms’.

        This method is used to check if a quantity is available without further
        calculations. For this reason, calculators should react to
        unknown/unsupported quantities by returning True, indicating that the
        quantity is not available.
        """

    def get_forces(atoms):
        """Return the forces."""

    def get_potential_energy(atoms=None, force_consistent=False):
        """Return total energy.

        Both the energy extrapolated to zero Kelvin and the energy consistent with
        the forces (the free energy) can be returned.
        """

    def get_stress(atoms):
        """Return the stress."""

    def create_subsys_from_atoms(self, subsys, atoms):
        """Create a CELL entry from the Atoms object.
        """
        for atom in atoms:
            subsys.COORD.add_DEFAULT_KEYWORD(atom.symbol + " " + str(atom.position[0]) + " " + str(atom.position[1]) + " " + str(atom.position[2]))
        cell = atoms.get_cell()
        A = cell[0, :]
        B = cell[1, :]
        C = cell[2, :]
        subsys.CELL._A = " " + str(A[0]) + " " + str(A[1]) + " " + str(A[2])
        subsys.CELL._B = " " + str(B[0]) + " " + str(B[1]) + " " + str(B[2])
        subsys.CELL._C = " " + str(C[0]) + " " + str(C[1]) + " " + str(C[2])

    def write_input_file(self):
        """Creates an input file for CP2K executable from the object tree
        defined in CP2K_INPUT
        """
        cp2k_input = self.CP2K_INPUT.print_input(-1)

        # Use one of the aliases for project name
        project_name = self.CP2K_INPUT.GLOBAL._PROJECT
        if project_name is None:
            project_name = self.CP2K_INPUT.GLOBAL._PROJECT_NAME

        # Write the file
        with open(self.input_path, 'w') as input_file:
            input_file.write(cp2k_input)

    def read_input_file(self, file_name):
        """Reads an existing CP2K input file and creates the corresponding
        object tree from it"""

        # Open the file
        with open(self.file_name, 'r') as input_file:
            pass

    def run(self):
        """Runs the input script."""
        self.write_input_file()
        command_list = []

        # MPI command and flags
        if self.mpi_on:
            command_list.append(self.mpi_command)
            self.mpi_flags["-n"] = self.mpi_n_processes
            for flag, value in self.mpi_flags.iteritems():
                command_list.append(str(flag))
                command_list.append(str(value))

        # CP2K command and flags
        self.cp2k_flags["-o"] = self.output_path
        self.cp2k_flags["-i"] = self.input_path

        command_list.append(self.cp2k_command)
        for flag, value in self.cp2k_flags.iteritems():
            command_list.append(str(flag))
            command_list.append(str(value))

        call(command_list, shell=False)

    #def reset(self):
        #"""Clear all information from old calculation."""
        #Calculator.reset(self)
        #self._release_force_env()

    #def set(self, **kwargs):
        #"""Set parameters like set(key1=value1, key2=value2, ...)."""
        #changed_parameters = Calculator.set(self, **kwargs)
        #if changed_parameters:
            #self.reset()

    #def write(self, label):
        #"""Write atoms, parameters and calculated properties into restart files."""
        #self.atoms.write(label + '_restart.traj')
        #self.parameters.write(label + '_params.ase')
        #open(label+'_results.ase', "w").write(repr(self.results))

    #def read(self, label):
        #"""Read atoms, parameters and calculated properties from restart files."""
        #from numpy import array
        #self.atoms = ase.io.read(label+'_restart.traj')
        #self.parameters = Parameters.read(label + '_params.ase')
        #self.results = eval(open(label+'_results.ase').read())

    #def calculate(self, atoms=None, properties=['energy'], system_changes=all_changes):
        #"""Do the calculation."""

        #Calculator.calculate(self, atoms, properties, system_changes)

        #if("numbers" in system_changes or "initial_magmoms" in system_changes):
            #self._release_force_env()

        #if(self._force_env_id is None):
            #self._create_force_env()

        #n_atoms = len(self.atoms)
        #if("cell" in system_changes):
            #cell = self.atoms.get_cell()
            #self._send("SET_CELL %d"%self._force_env_id)
            #self._send(" ".join(["%.10f"%x for x in cell.flat]))
            #assert(self._recv() == "* READY")

        #if("positions" in system_changes):
            #self._send("SET_POS %d"%self._force_env_id)
            #self._send("%d"%(3*n_atoms))
            #for pos in self.atoms.get_positions():
                #self._send("%.10f   %.10f   %.10f"%(pos[0], pos[1], pos[2]))
            #self._send("*END")
            #assert(float(self._recv()) >= 0) # max change -> ignore
            #assert(self._recv() == "* READY")

        #self._send("EVAL_EF %d"%self._force_env_id)
        #assert(self._recv() == "* READY")

        #self._send("GET_E %d"%self._force_env_id)
        #self.results['energy'] = float(self._recv()) * Hartree
        #assert(self._recv() == "* READY")

        #forces = np.zeros(shape=(n_atoms,3) )
        #self._send("GET_F %d"%self._force_env_id)
        #assert(int(self._recv()) == 3*n_atoms)
        #for i in range(n_atoms):
            #line = self._recv()
            #forces[i,:] = [float(x) for x in line.split()]
        #assert(self._recv() == "* END")
        #assert(self._recv() == "* READY")
        #self.results['forces'] = forces * Hartree / Bohr

        #self._send("GET_STRESS %d"%self._force_env_id)
        #line = self._recv()
        #assert(self._recv() == "* READY")

        #stress = np.array([float(x) for x in line.split()]).reshape(3, 3)
        #assert(np.all(stress == np.transpose(stress)))  # should be symmetric
        ## Convert 3x3 stress tensor to Voigt form as required by ASE
        #stress = np.array([stress[0, 0], stress[1, 1], stress[2, 2],
                           #stress[1, 2], stress[0, 2], stress[0, 1]])
        #self.results['stress'] = stress * Hartree / Bohr**3

        #self.write(self.label)  # TODO: this should not be called so often

    #def _create_force_env(self):
        #assert(self._force_env_id is None)
        #inp = self._generate_input()

        #if(self._debug):
            #print inp
        #fd, inp_fn = mkstemp(suffix=".inp")
        #f = os.fdopen(fd, "w")
        #f.write(inp)
        #f.close()

        #label_dir = path.dirname(self.label)
        #if(len(label_dir)>0 and not path.exists(label_dir)):
            #print "Creating directory: "+label_dir
            #os.makedirs(label_dir)  # cp2k expects dirs to exist
        #out_fn = self.parameters.txt
        #if(out_fn == "-"):
            #out_fn = "__STD_OUT__"
        #self._send("LOAD %s %s"%(inp_fn, out_fn))
        #self._force_env_id = int(self._recv())
        #assert(self._force_env_id > 0)
        #assert(self._recv() == "* READY")
        #os.remove(inp_fn)

    #def _release_force_env(self):
        #if(self._force_env_id):
            #self._send("DESTROY %d"%self._force_env_id)
            #assert(self._recv() == "* READY")
            #self._force_env_id = None

    #def _generate_input(self):
        #p = self.parameters

        #output = "!!!! Generated by ASE !!!!\n"
        #output += "&GLOBAL\n"
        #output += "PROJECT %s\n"%self.label
        #output += "&END GLOBAL\n"

        #output += "&FORCE_EVAL\n"
        #output += "&PRINT\n"
        #output += "  &STRESS_TENSOR ON\n"
        #output += "  &END STRESS_TENSOR\n"
        #output += "&END PRINT\n"

        #output += "METHOD Quickstep\n"
        #output += "STRESS_TENSOR ANALYTICAL\n"

        #output += "&SUBSYS\n"

        ## determine pseudo-potential
        #potential = p.pseudo_potential
        #if(p.pseudo_potential.lower() == "auto"):
            #if(p.xc.upper() == "LDA"):
                #potential = "GTH-PADE"
            #elif(p.xc.upper() in ("PADE", "BP", "BLYP", "PBE",)):
                #potential = "GTH-"+p.xc.upper()
            #else:
                #warn("No matching pseudo potential found, falling back to GTH-PBE", RuntimeWarning)
                #potential = "GTH-PBE" # fall back

        ## write atomic kinds
        #valence_electrons = self._parse_basis_set()
        #for elem in set(self.atoms.get_chemical_symbols()):
            #output += "&KIND %s\n"%elem
            #output += "  BASIS_SET %s\n"%p.basis_set
            #q = valence_electrons[(elem, p.basis_set)]
            #output += "  POTENTIAL %s-q%d\n"%(potential, q)
            #output += "&END KIND\n"

        ## write coords
        #output += "&COORD\n"
        #n_electrons = 0
        #for elem, pos in zip(self.atoms.get_chemical_symbols(), self.atoms.get_positions()):
            #n_electrons += valence_electrons[(elem, p.basis_set)]
            #output += "  %s  %.10f   %.10f   %.10f\n"%(elem, pos[0], pos[1], pos[2])
        #output += "&END COORD\n"

        ## write cell
        #output += "&CELL\n"
        #pbc = "".join([a for a,b in zip("XYZ",self.atoms.get_pbc()) if b])
        #if(len(pbc)==0): pbc = "NONE"
        #output += "  PERIODIC %s\n"%pbc
        #cell = self.atoms.get_cell()
        #output += "  A  %.10f   %.10f   %.10f\n"%(cell[0,0], cell[0,1], cell[0,2])
        #output += "  B  %.10f   %.10f   %.10f\n"%(cell[1,0], cell[1,1], cell[1,2])
        #output += "  C  %.10f   %.10f   %.10f\n"%(cell[2,0], cell[2,1], cell[2,2])
        #output += "&END CELL\n"
        #output += "&END SUBSYS\n"

        ## write DFT-section
        #output += "&DFT\n"
        #output += "BASIS_SET_FILE_NAME %s\n"%p.basis_set_file
        #output += "POTENTIAL_FILE_NAME %s\n"%p.potential_file
        ##if(any(atoms.get_initial_magnetic_moments()!=0)):
        #if(n_electrons%2 != 0): #TODO is this the proper way?
            #output += "SPIN_POLARIZED .TRUE.\n"
        #if(p.charge != 0):
            #output += "CHARGE %d\n"%p.charge

        #output += "&XC\n"
        #output += "  &XC_FUNCTIONAL %s\n"%p.xc
        #output += "  &END XC_FUNCTIONAL\n"
        #output += "&END XC\n"

        #output += "&MGRID\n"
        #output += "  CUTOFF [eV] %.3f\n"%p.cutoff
        #output += "&END MGRID\n"

        #output += "&SCF\n"
        #output += "  MAX_SCF %d\n"%p.max_scf
        #output += "&END SCF\n"

        #output += "&END DFT\n"
        #output += "&END FORCE_EVAL\n"

        #return(output)

    #def _send(self, line):
        #"""Send a line to the cp2k_shell"""
        #assert(self._child.poll() is None)  # child process still alive?
        #if(self._debug):
            #print("Sending: "+line)
        #self._child.stdin.write(line+"\n")

    #def _recv(self):
        #"""Receive a line from the cp2k_shell"""
        #assert(self._child.poll() is None)  # child process still alive?
        #line = self._pipe.readline().strip()
        #if(self._debug):
            #print("Received: "+line)
        #return(line)
