### ADD DLL ###
psspy.addmodellibrary(path_file_dlls+file)

### ADD DYR ###
psspy.dyre_new([1,1,1,1],path_model+dyr_file)

### GET MODEL NAME SUBJECT TO WIND MACHINE ###
ierr,aux_name=psspy.windmnam(gens[0][0],gens[0][1],'WAUX')

### GET MODEL ADDRESS(ZERO POSITIOMN) ###
_,aux_con0=psspy.windmind(gens[0][0],gens[0][1],'WAUX','CON')
_,aux_icon0=psspy.windmind(gens[0][0],gens[0][1],'WAUX','ICON')
_,aux_var0=psspy.windmind(gens[0][0],gens[0][1],'WAUX','VAR')

### GET VALUES FROM DYNAMICS ###
"""
Wanted value can be derived by modifying value of aux_con0, var0 and icon0 
"""
_,aux_con_value=psspy.dsrval('CON',aux_con0)
_,aux_var_value=psspy.dsrval('VAR',aux_var0)
_,aux_icon_value=psspy.dsival('ICON',aux_icon0)

## CHANGE ICON, CON, VAR DURING DYNAMICS ###
## Change STR
ierr=psspy.change_wnmod_chricn(gens[0][0],gens[0][1],aux_name,icon_num,'STR_CHANGE') ## icon_num to change relative to the start of the block (1 for ICON(I), 2 for ICON(I+1))
## CHANGE ICON
ierr=psspy.change_wnmod_icon(gens[0][0],gens[0][1],aux_name,icon_num,value) ## icon_num to change relative to the start of the block (1 for ICON(I), 2 for ICON(I+1))
## CHANGE CON
ierr=psspy.change_wnmod_icon(gens[0][0],gens[0][1],aux_name,icon_num,value) ## icon_num to change relative to the start of the block (1 for CON(J), 2 for CON(J+1))
## CHANGE VAR
ierr=psspy.change_wnmod_var(gens[0][0],gens[0][1],aux_name,icon_num,'STR_CHANGE') ## icon_num to change relative to the start of the block (1 for VAR(J), 2 for VAR(J+1))
