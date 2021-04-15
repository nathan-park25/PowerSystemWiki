	
def robust_solve(lockTaps=False, verbose=False):
	'''
	Attempts to find a load flow solution
		lockTaps	Boolean, whether taps are locked for load flow
		
		verbose		Boolean, whether debug information is printed
	
	Returns True if solution found, else False
	
	further information on robust load flow: 
		https://static.dc.siemens.com/datapool/us/SmartGrid/docs/pti/2012March/PDFs/Dealing_with_power_flow_solution_difficulties.pdf
	
	TODO:
		Try to implement the below algorithm:
			ROBUST SOLUTION REPORT
			----------------------
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 3721.95 MVA
			Recording new set of best known settings
			Reloading original case and settings
			(FDNS.1) Straight Solve (try to solve directly)
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 3721.95 MVA
			Reloading original case and settings
			(FDNS.2) Flat Solve (Try to solve by flat-starting)
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 7804.72 MVA
			Reloading original case and settings
			(FDNS.3) Smooth Solve (try to solve by smoothing angles/voltages)
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 16469.16 MVA
			Reloading original case and settings
			(FDNS.4) Slow Solve (try to solve by loosening soln params)
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 16469.16 MVA
			Reloading original case and settings
			(FDNS.5) Loose Solve (try to solve by phasing-in controls)
			Locking all adjustable controls
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 2140.25 MVA
			Recording new set of best known settings
			Reloading original case and settings
			(FNSL.1) Straight Solve (try to solve directly)
			Solving with FNSL solution
			Solution result: 2 (BlownUp) with Max mismatch of 13080.64 MVA
			Reloading original case and settings
			(FDNS.2) Flat Solve (Try to solve by flat-starting)
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 7804.72 MVA
			Reloading original case and settings
			(FDNS.3) Smooth Solve (try to solve by smoothing angles/voltages)
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 16469.16 MVA
			Reloading original case and settings
			(FDNS.4) Slow Solve (try to solve by loosening soln params)
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 16469.16 MVA
			Reloading original case and settings
			(FDNS.5) Loose Solve (try to solve by phasing-in controls)
			Locking all adjustable controls
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 2140.25 MVA
			Reloading original case and settings
			(NSOL.1) Straight Solve (try to solve directly)
			Solving with NSOL solution
			Solution result: 2 (BlownUp) with Max mismatch of 13945.14 MVA
			Reloading original case and settings
			(FDNS.2) Flat Solve (Try to solve by flat-starting)
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 7804.72 MVA
			Reloading original case and settings
			(FDNS.3) Smooth Solve (try to solve by smoothing angles/voltages)
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 16469.16 MVA
			Reloading original case and settings
			(FDNS.4) Slow Solve (try to solve by loosening soln params)
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 16469.16 MVA
			Reloading original case and settings
			(FDNS.5) Loose Solve (try to solve by phasing-in controls)
			Locking all adjustable controls
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 2140.25 MVA
			Reloading original case and settings
			(MSLV.1) Straight Solve (try to solve directly)
			Solving with MSLV solution
			Solution result: 2 (BlownUp) with Max mismatch of 35278450.69 MVA
			Reloading original case and settings
			(FDNS.2) Flat Solve (Try to solve by flat-starting)
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 7804.72 MVA
			Reloading original case and settings
			(FDNS.3) Smooth Solve (try to solve by smoothing angles/voltages)
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 16469.16 MVA
			Reloading original case and settings
			(FDNS.4) Slow Solve (try to solve by loosening soln params)
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
			Solving with FDNS solution
			Solution result: 2 (BlownUp) with Max mismatch of 16469.16 MVA
			Reloading original case and settings
			(FDNS.5) Loose Solve (try to solve by phasing-in controls)
			Locking all adjustable controls
			Increasing iteration limit to 200
			Increasing tolerance to 10.0 MVA
			Lowering acceleration factor to 0.4
			Smoothing angles and voltages at 1 buses
		
	'''
	# backup case
	tmp_case = os.getcwd() + "\\temp_loadflow_%08d.sav" % random.randint(0,99999999)
	psspy.save(tmp_case)
	
	# try basic solve
	if verbose: print(" Basic solve")
	sol_params = {
		'intgar2':200,	# max iteration [20]
		'realar5':1.0,	# ACCN [1.0]
		'realar6':0.1,	# solution tolerance [0.1]
	}
	NR_params = [0]*8 if lockTaps else [1,0,0,1,1,0,0,0] # standard solve
	psspy.solution_parameters_4(**sol_params) 
	psspy.fnsl(NR_params) 
	if verbose: print("  - Mismatch = %.1fMVA; Solved = %s" % (psspy.sysmsm(),psspy.solved()))
	
	# record sysmsm
	best_sysmsm = psspy.sysmsm()
	best_sol_params = {}
	best_NR_params = [0]*8 if lockTaps else [1,0,0,1,1,0,0,0]
	
	# try with slower Newton Raphson
	if psspy.solved() != 0:
		psspy.case(tmp_case)
		if verbose: print(" NR with modified params 1")
		sol_params = {
				'intgar2':200, 	# max iteration [20]
				'realar5':0.1,	# ACCN [1.0]
				'realar10':0.85,	# constant power load threshold [0.7]
				'realar6':2.0,	# solution tolerance [0.1]
			}	
		NR_params = [0]*8 # locked taps/shunts
		psspy.solution_parameters_4(**sol_params) 
		psspy.fnsl(NR_params)
		if verbose: print("  - Mismatch = %.1fMVA; Solved = %s" % (psspy.sysmsm(),psspy.solved()))
		if psspy.sysmsm() < best_sysmsm:
			# record sysmsm
			best_sysmsm = psspy.sysmsm()
			best_sol_params = sol_params
			best_NR_params = NR_params
		if verbose: print(" Unlocked shunts")
		NR_params = [0]*8 if lockTaps else [0,0,0,1,1,0,0,0] # locked taps
		psspy.fnsl(NR_params)
		if verbose: print("  - Mismatch = %.1fMVA; Solved = %s" % (psspy.sysmsm(),psspy.solved()))
		if psspy.sysmsm() < best_sysmsm:
			# record sysmsm
			best_sysmsm = psspy.sysmsm()
			best_sol_params = sol_params
			best_NR_params = NR_params
		if verbose: print(" Unlocked taps&shunts")
		NR_params = [0]*8 if lockTaps else [1,0,0,1,1,0,0,0] # standard solve
		psspy.fnsl(NR_params)
		if verbose: print("  - Mismatch = %.1fMVA; Solved = %s" % (psspy.sysmsm(),psspy.solved()))
		if psspy.sysmsm() < best_sysmsm:
			# record sysmsm
			best_sysmsm = psspy.sysmsm()
			best_sol_params = sol_params
			best_NR_params = NR_params
	
	# try with Fixed Decoupled Newton Raphson
	if psspy.solved() != 0:
		psspy.case(tmp_case)
		if verbose: print(" FDNS with modified params 1")
		sol_params = {
				'intgar2':200, 		# max iteration [20]
				'realar5':0.4,		# ACCN [1.0]
				'realar6':1.0,		# solution tolerance [0.1]
				'realar3':0.4,		# MSLV acc factor [1.0]
				'realar17':0.1,		# NR voltage-controlled bus Q msm tolerance
				'realar18':1E-5,	# NR voltage-controlled bus V error tolerance
			}	
		NR_params = [0]*8 # locked taps/shunts
		NR_params[6] = 100 # apply var limits on iter 100
		psspy.solution_parameters_4(**sol_params) 
		psspy.fdns(NR_params)
		if verbose: print("  - Mismatch = %.1fMVA; Solved = %s" % (psspy.sysmsm(),psspy.solved()))
		if psspy.sysmsm() < best_sysmsm:
			# record sysmsm
			best_sysmsm = psspy.sysmsm()
			best_sol_params = sol_params
			best_NR_params = NR_params
		if verbose: print(" Unlocked shunts")
		NR_params = [0]*8 if lockTaps else [0,0,0,1,1,0,0,0] # locked taps
		psspy.fdns(NR_params)
		if verbose: print("  - Mismatch = %.1fMVA; Solved = %s" % (psspy.sysmsm(),psspy.solved()))
		if psspy.sysmsm() < best_sysmsm:
			# record sysmsm
			best_sysmsm = psspy.sysmsm()
			best_sol_params = sol_params
			best_NR_params = NR_params
		if verbose: print(" Unlocked taps&shunts")
		NR_params = [0]*8 if lockTaps else [1,0,0,1,1,0,0,0] # standard solve
		psspy.fdns(NR_params)
		if verbose: print("  - Mismatch = %.1fMVA; Solved = %s" % (psspy.sysmsm(),psspy.solved()))
		if psspy.sysmsm() < best_sysmsm:
			# record sysmsm
			best_sysmsm = psspy.sysmsm()
			best_sol_params = sol_params
			best_NR_params = NR_params
	
	# try a different swing bus
	if psspy.solved() != 0:
		swing_bus = get_swing_bus()
		new_swing_bus = swing_bus
		for bus in SWINGBUSES:
			psspy.case(tmp_case)
			if psspy.busexs(bus) == 1: continue
			ierr, btype = psspy.busint(bus,'TYPE')
			if btype != 2: continue
			ierr = psspy.bus_chng_4(swing_bus,0,intgar1=2)
			if verbose: print(" Trying %d as swing bus" % (bus))
			psspy.bus_chng_4(bus,0,intgar1=3)
			
			psspy.solution_parameters_4(**best_sol_params)
			psspy.fnsl(best_NR_params)
			if verbose: print("  - Mismatch = %.1fMVA; Solved = %s" % (psspy.sysmsm(),psspy.solved()))
			
			if psspy.solved() == 0: break
			
			if psspy.sysmsm() < best_sysmsm:
				# record sysmsm
				best_sysmsm = psspy.sysmsm()
				new_swing_bus = bus
	
	if psspy.solved() == 0:
		os.remove(tmp_case)
		return True
	else:
		# no solution found - give up
		if verbose: print(" Could not find load flow solution")
		if verbose: print(" Best mismatch of %.1fMVA: params=%s; fnsl=%s; swing_bus=%d" % (best_sysmsm,best_sol_params,best_NR_params,new_swing_bus))
		psspy.case(tmp_case)
		os.remove(tmp_case)
		return False
