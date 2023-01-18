# -*- coding: utf-8 -*-
"""

@author: Felipe Henao
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:46:44 2022

@author: Felipe Henao
"""
from operator import length_hint
import pandas as pd
import math

###############################################################################
###############################################################################

"""RECIBIR DATOS PICO"""

def Recibir_Lmax(ruta_archivo):
    output_dataframe = pd.DataFrame()
    archivo = open(ruta_archivo, "r")
    datos = [line.rstrip('\n').split(':') for line in archivo]
    for n in range(9, length_hint(datos)-1):
        out = pd.DataFrame()
        valor=datos[n][3]
        fecha=datos[n][0]
        out.loc[(n, 'Fecha')] = fecha[0:10] 
        if valor[4:9]!='':
            out.loc[(n, 'Lmax (dBA)')] = float(valor[4: 9].replace(",","."))
        else:
            out.loc[(n, 'Lmax (dBA)')] = ''
        output_dataframe = pd.concat([output_dataframe, out], axis=0)
    archivo.close()
    return output_dataframe

###############################################################################
###############################################################################

"""RECIBIR DATOS IMPULSO"""

def Recibir_impulso(ruta_archivo):
    output_dataframe = pd.DataFrame()
    archivo = open(ruta_archivo, "r")
    datos = [line.rstrip('\n').split(':') for line in archivo]
    for n in range(13, length_hint(datos)):
        out = pd.DataFrame()
        valores=datos[n][0]
        c = '\t'
        lst = []
        if(length_hint(valores)!=0):    
            for pos,char in enumerate(valores):
                if(char == c):
                    lst.append(pos)
            out.loc[(n, 'Fecha')] = valores[0:lst[0]] 
            if valores[lst[0]+1:lst[1]]!='':    
                out.loc[(n, 'Ld (dBA) imp ')] = float(valores[lst[0]+1:lst[1]]
                                                      .replace(",","."))
            else:
                out.loc[(n, 'Ld (dBA) imp ')] = ''
            if valores[lst[1]+1:]!='':
                out.loc[(n, 'Ln (dBA) imp ')] = float(valores[lst[1]+1:]
                                                      .replace(",","."))
            else:
                out.loc[(n, 'Ln (dBA) imp ')] = ''
            output_dataframe = pd.concat([output_dataframe, out], axis=0)
    archivo.close()
    return output_dataframe

###############################################################################
###############################################################################

"""RECIBIR DATOS DE Ln y Ld"""

def Recibir_Ld_Ln(ruta_archivo):
    output_Ld = pd.DataFrame()
    output_Ln = pd.DataFrame()
    archivo = open(ruta_archivo, "r")
    datos = [line.rstrip('\n').split(':') for line in archivo]
    i=0
    for n in range(11, length_hint(datos)):
        out = pd.DataFrame()
        valores=datos[n][0]
        c = '\t'
        lst = []
        if(valores!='Período\tNoche0627_Ln (Ln)'):    
            for pos,char in enumerate(valores):
                if(char == c):
                    lst.append(pos)
            out.loc[(n, 'Fecha')] = valores[0:lst[0]] 
            if valores[lst[0]+1:lst[1]]!='':
                out.loc[(n, 'Ld*')] = float(valores[lst[0]+1:lst[1]]
                                           .replace(",","."))
            else:
                out.loc[(n, 'Ld*')] = ''
            if valores[lst[1]+1:lst[2]]!='':
                out.loc[(n, 'SEL Ld')] = float(valores[lst[1]+1:lst[2]]
                                               .replace(",","."))
            else:
                out.loc[(n, 'SEL Ld')] = ''
            if valores[lst[2]+1:lst[3]]!='':
                out.loc[(n, 'Lmin Ld')] = float(valores[lst[2]+1:lst[3]]
                                                .replace(",","."))
            else:
                out.loc[(n, 'Lmin Ld')] = ''
            if valores[lst[3]+1:lst[4]]!='':
                out.loc[(n, 'Lmax Ld')] = float(valores[lst[3]+1:lst[4]]
                                                .replace(",","."))
            else:
                out.loc[(n, 'Lmax Ld')] = ''
            if valores[lst[4]+1:lst[5]]!='':
                out.loc[(n, 'StdDev Ld')] = float(valores[lst[4]+1:lst[5]]
                                                  .replace(",","."))
            else:
                out.loc[(n, 'StdDev Ld')] = ''
            if valores[lst[5]+1:lst[6]]!='':
                out.loc[(n, 'L90 Ld')] = float(valores[lst[5]+1:lst[6]]
                                               .replace(",","."))
            else:
                out.loc[(n, 'L90 Ld')] = ''
            if valores[lst[6]+1:lst[7]]!='':
                out.loc[(n, 'L50 Ld')] = float(valores[lst[6]+1:lst[7]]
                                               .replace(",","."))
            else:
                out.loc[(n, 'L50 Ld')] = ''
            if valores[lst[7]+1:lst[8]]!='':
                out.loc[(n, 'L20 Ld')] = float(valores[lst[7]+1:lst[8]]
                                               .replace(",","."))
            else:
                out.loc[(n, 'L20 Ld')] = ''
            if valores[lst[8]+1:lst[9]]!='':
                out.loc[(n, 'L10 Ld')] = float(valores[lst[8]+1:lst[9]]
                                               .replace(",","."))
            else:
                out.loc[(n, 'L10 Ld')] = ''
            if valores[lst[9]+1:lst[10]]!='':
                out.loc[(n, 'L5 Ld')] = float(valores[lst[9]+1:lst[10]]
                                              .replace(",","."))
            else:
                out.loc[(n, 'L5 Ld')] = ''
            output_Ld = pd.concat([output_Ld, out], axis=0)
        else:
            i=n+4
            break
    for n in range(i, length_hint(datos)):
        out = pd.DataFrame()
        valores=datos[n][0]
        c = '\t'
        lst = []
        if(length_hint(valores)!=0):    
            for pos,char in enumerate(valores):
                if(char == c):
                    lst.append(pos)
            out.loc[(n, 'Fecha')] = valores[0:lst[0]] 
            if valores[lst[0]+1:lst[1]]!='':
                out.loc[(n, 'Ln*')] = float(valores[lst[0]+1:lst[1]]
                                           .replace(",","."))
            else:
                out.loc[(n, 'Ln*')] = ''
            if valores[lst[1]+1:lst[2]]!='':
                out.loc[(n, 'SEL Ln')] = float(valores[lst[1]+1:lst[2]]
                                               .replace(",","."))
            else:
                out.loc[(n, 'SEL Ln')] = ''
            if valores[lst[2]+1:lst[3]]!='':
                out.loc[(n, 'Lmin Ln')] = float(valores[lst[2]+1:lst[3]]
                                                .replace(",","."))
            else:
                out.loc[(n, 'Lmin Ln')] = ''
            if valores[lst[3]+1:lst[4]]!='':
                out.loc[(n, 'Lmax Ln')] = float(valores[lst[3]+1:lst[4]]
                                                .replace(",","."))
            else:
                out.loc[(n, 'Lmax Ln')] = ''
            if valores[lst[4]+1:lst[5]]!='':
                out.loc[(n, 'StdDev Ln')] = float(valores[lst[4]+1:lst[5]]
                                                  .replace(",","."))
            else:
                out.loc[(n, 'StdDev Ln')] = ''
            if valores[lst[5]+1:lst[6]]!='':
                out.loc[(n, 'L90 Ln')] = float(valores[lst[5]+1:lst[6]]
                                               .replace(",","."))
            else:
                out.loc[(n, 'L90 Ln')] = ''
            if valores[lst[6]+1:lst[7]]!='':
                out.loc[(n, 'L50 Ln')] = float(valores[lst[6]+1:lst[7]]
                                               .replace(",","."))
            else:
                out.loc[(n, 'L50 Ln')] = ''
            if valores[lst[7]+1:lst[8]]!='':
                out.loc[(n, 'L20 Ln')] = float(valores[lst[7]+1:lst[8]]
                                               .replace(",","."))
            else:
                out.loc[(n, 'L20 Ln')] = ''
            if valores[lst[8]+1:lst[9]]!='':
                out.loc[(n, 'L10 Ln')] = float(valores[lst[8]+1:lst[9]]
                                               .replace(",","."))
            else:
                out.loc[(n, 'L10 Ln')] = ''
            if valores[lst[9]+1:lst[10]]!='':
                out.loc[(n, 'L5 Ln')] = float(valores[lst[9]+1:lst[10]]
                                              .replace(",","."))
            else:
                out.loc[(n, 'L5 Ln')] = ''
            output_Ln = pd.concat([output_Ln, out], axis=0)
        else:
            break  
    return(output_Ld,output_Ln)

###############################################################################
###############################################################################

"""RECIBIR DATOS DE TERCIOS DE OCTAVA"""

def Recibir_ter_oct(ruta_archivo):
    tamaño=length_hint(ruta_archivo)
    output_final = pd.DataFrame()
    i=2
    lst = []
    f=['20Hz','25Hz','31.5Hz','40Hz','50Hz','63Hz','80Hz','100Hz','125Hz','160Hz',
       '200Hz','250Hz','315Hz','400Hz','500Hz','630Hz','800Hz','1KHz','1.25KHz',
       '1.6KHz','2KHz','2.5KHz','3.15KHz','4KHz','5KHz','6.3KHz','8KHz','10KHz',
       '12.5KHz','16KHz','20KHz']
    corr=[-50.5,-44.7,-39.4,-34.6,-30.2,-26.2,-22.5,-19.1,-16.1,-13.4,-10.9,-8.6,
          -6.6,-4.8,-3.2,-1.9,-0.8,0,0.6,1,1.2,1.3,1.2,1,0.5,-0.1,-1.1,-2.5,-4.3,
          -6.6,-9.3]
    for p in range(0,8):
        lst.append(ruta_archivo[0:tamaño-1]+str(i))
        i=i+1
    for u in range(i,33):
        lst.append(ruta_archivo[0:tamaño-2]+str(i))
        i=i+1
    for o in range(0,length_hint(lst)):        
        output_dataframe = pd.DataFrame()
        archivo = open(lst[o], "r")
        datos = [line.rstrip('\n').split(':') for line in archivo] 
        for n in range(13, length_hint(datos)):
            out = pd.DataFrame()
            valores=datos[n][0]
            c = '\t'
            lst2 = []
            if(length_hint(valores)!=0):    
                for pos,char in enumerate(valores):
                    if(char == c):
                        lst2.append(pos)
                out.loc[(n, 'Fecha '+ f[o])] = valores[0:lst2[0]] 
                if valores[lst2[0]+1:lst2[1]]!='':
                    num=float(valores[lst2[0]+1:lst2[1]].replace(",","."))+corr[o]
                    if (num>0): 
                        out.loc[(n, 'Ld' + f[o])] = num
                    else:
                        out.loc[(n, 'Ld' + f[o])] = 0
                else:
                    out.loc[(n, 'Ld' + f[o])] = ''
                if valores[lst2[1]+1:]!='':
                    num= float(valores[lst2[1]+1:].replace(",","."))+corr[o]
                    if (num>0): 
                        out.loc[(n, 'Ln' + f[o])] = num
                    else:
                        out.loc[(n, 'Ln' + f[o])] = 0      
                else:
                    out.loc[(n, 'Ln' + f[o])] = ''
                output_dataframe = pd.concat([output_dataframe, out], axis=0)
        output_final= pd.concat([output_final, output_dataframe], axis=1)
        archivo.close()
    return output_final

###############################################################################
###############################################################################

"""RECIBIR CORRECCIONES TONALES - TERCIOS DE OCTAVA"""

def Recibir_corr_dia(rut):
    fd=['Ld20Hz','Ld25Hz','Ld31.5Hz','Ld40Hz','Ld50Hz','Ld63Hz','Ld80Hz','Ld100Hz',
            'Ld125Hz','Ld160Hz','Ld200Hz','Ld250Hz','Ld315Hz','Ld400Hz','Ld500Hz',
            'Ld630Hz','Ld800Hz','Ld1KHz','Ld1.25KHz','Ld1.6KHz','Ld2KHz','Ld2.5KHz',
            'Ld3.15KHz','Ld4KHz','Ld5KHz','Ld6.3KHz','Ld8KHz','Ld10KHz','Ld12.5KHz',
            'Ld16KHz','Ld20KHz']
    fn=[]
    freq_index=[]
    for n in range(0,length_hint(fd)):
        fn.append(fd[n].replace("Ld","Ln"))
        freq_index.append(fd[n].replace("Ld",""))
    ter_oct=Recibir_ter_oct(rut)
    ter_oct.reset_index(drop=True, inplace=True)
    tonos=[]
    correcciones=[]
    Ld=[[],[]]
    cd=[[],[],[],[]]
    for x in range(0,length_hint(ter_oct)):
        if ter_oct.loc[(x,'Ld20Hz')]!='':
            for n in range(0,length_hint(fd)):
                Ld[0].append(round(ter_oct.loc[(x,fd[n])],2))
            for n in range(0,length_hint(Ld[0])-2):
                if Ld[0][n+1]>Ld[0][n] and Ld[0][n+1]>Ld[0][n+2]:
                    cd[0].append(round(Ld[0][n+1]-((Ld[0][n]+Ld[0][n+2])/2),2))
                else:
                    cd[0].append(0)
            tonos.append(cd[0])
            for n in range(0,8):
                if cd[0][n]!=0:
                    if cd[0][n]>=12:
                        cd[2].append(6)
                    elif cd[0][n]>=8:
                        cd[2].append(3)
                    else:
                        cd[2].append(0)
                else:
                    cd[2].append(0)  
            for n in range(8,13):
                if cd[0][n]!=0:
                    if cd[0][n]>=8:
                        cd[2].append(6)
                    elif cd[0][n]>=5:
                        cd[2].append(3)
                    else:
                        cd[2].append(0)
                else:
                    cd[2].append(0)
            for n in range(13,29):
                if cd[0][n]!=0:
                    if cd[0][n]>=5:
                        cd[2].append(6)
                    elif cd[0][n]>=3:
                        cd[2].append(3)
                    else:
                        cd[2].append(0)
                else:
                    cd[2].append(0)
            correcciones.append(cd[2])
            
        else:
            correcciones.append('')
            tonos.append('')
            
            
        if ter_oct.loc[(x,'Ln20Hz')]!='':
            for n in range(0,length_hint(fd)):
                Ld[1].append(round(ter_oct.loc[(x,fn[n])],2))
            for n in range(0,length_hint(Ld[1])-2):
                if Ld[1][n+1]>Ld[1][n] and Ld[1][n+1]>Ld[1][n+2]:
                    cd[1].append(round(Ld[1][n+1]-((Ld[1][n]+Ld[1][n+2])/2),2))
                else:
                    cd[1].append(0)
            tonos.append(cd[1])
            for n in range(0,8):
                if cd[1][n]!=0:
                    if cd[1][n]>=12:
                        cd[3].append(6)
                    elif cd[1][n]>=8:
                        cd[3].append(3)
                    else:
                        cd[3].append(0)
                else:
                    cd[3].append(0)  
            for n in range(8,13):
                if cd[1][n]!=0:
                    if cd[1][n]>=8:
                        cd[3].append(6)
                    elif cd[1][n]>=5:
                        cd[3].append(3)
                    else:
                        cd[3].append(0)
                else:
                    cd[3].append(0)
            for n in range(13,29):
                if cd[1][n]!=0:
                    if cd[1][n]>=5:
                        cd[3].append(6)
                    elif cd[1][n]>=3:
                        cd[3].append(3)
                    else:
                        cd[3].append(0)
                else:
                    cd[3].append(0)

            correcciones.append(cd[3])
            Ld=[[],[]]
            cd=[[],[],[],[]]
        else:
            correcciones.append('')
            tonos.append('')
            Ld=[[],[]]
            cd=[[],[],[],[]]

    n=0
    o=0
    fecha=[]
    tonos_df = pd.DataFrame()
    corre_df = pd.DataFrame()
    for g in range(0,length_hint(ter_oct)):
        fecha.append(ter_oct.loc[(g,'Fecha 20Hz')])
        
    for g in range(0,length_hint(tonos)):
        try:
            if tonos[o]!='':
                tonos_d = pd.DataFrame(tonos[o], index=[freq_index[1:30]],
                                        columns=pd.MultiIndex.from_product([[fecha[n]],
                                                                            ['Corr D']]))
                corre_d = pd.DataFrame(correcciones[o], index=[freq_index[1:30]],
                                        columns=pd.MultiIndex.from_product([[fecha[n]],
                                                                            ['Corr D']]))
            else:
                tonos_d = pd.DataFrame('', index=[freq_index[1:30]],
                                        columns=pd.MultiIndex.from_product([[fecha[n]],
                                                                            ['Corr D']]))
                corre_d = pd.DataFrame('', index=[freq_index[1:30]],
                                        columns=pd.MultiIndex.from_product([[fecha[n]],
                                                                            ['Corr D']]))           
            if tonos[o+1]!='':                                                              
            
                tonos_n = pd.DataFrame(tonos[o+1], index=[freq_index[1:30]],
                                        columns=pd.MultiIndex.from_product([[fecha[n]],
                                                                            ['Corr N']]))
                corre_n = pd.DataFrame(correcciones[o+1], index=[freq_index[1:30]],
                                        columns=pd.MultiIndex.from_product([[fecha[n]],
                                                                            ['Corr N']]))
            else:
                tonos_n = pd.DataFrame('', index=[freq_index[1:30]],
                                        columns=pd.MultiIndex.from_product([[fecha[n]],
                                                                            ['Corr N']]))
                corre_n = pd.DataFrame('', index=[freq_index[1:30]],
                                        columns=pd.MultiIndex.from_product([[fecha[n]],
                                                                            ['Corr N']]))
            tonos_df=pd.concat([tonos_df,tonos_d,tonos_n], axis=1)
            corre_df=pd.concat([corre_df,corre_d,corre_n], axis=1)
            o=o+2
            n=n+1
        except IndexError:
            break
    vd=[]
    vn=[]
    for n in range(0,length_hint(correcciones),2):
        if correcciones[n]!='':
            vd.append(max(correcciones[n]))
        else:
            vd.append('')
        if correcciones[n+1]!='':
            vn.append(max(correcciones[n+1]))
        else:
            vn.append('')   
    penal_d = pd.DataFrame(vd, index =[fecha],columns =['Ld'])
    penal_n =pd.DataFrame(vn, index =[fecha],columns =['Ln'])
    penal_df=pd.concat([penal_d,penal_n],axis=1)    
    return(vd,vn,penal_df)
    
  
##############################################################################
##############################################################################

def Recibir_ki(Ld,Ln,Limp_df):
    kid=[]
    kin=[]
    fecha_d=[]
    fecha_n=[]
    kid_df = pd.DataFrame()
    kin_df = pd.DataFrame()
    for g in range(0,length_hint(Ld)):
        fecha_d.append(Ld.loc[(g,'Fecha')])
    for g in range(0,length_hint(Ln)):
        fecha_n.append(Ln.loc[(g,'Fecha')])
    for n in range(0,length_hint(Ld)):
        if Ld.loc[(n,'Ld*')]!='' and Limp_df.loc[(n,'Ld (dBA) imp ')]!='':
            if Limp_df.loc[(n,'Ld (dBA) imp ')]-Ld.loc[(n,'Ld*')]<3:
                kid.append(0)
            elif Limp_df.loc[(n,'Ld (dBA) imp ')]-Ld.loc[(n,'Ld*')]<6:
                kid.append(3)
            else:
                kid.append(6)
        else:
            kid.append('')
        if Ln.loc[(n,'Ln*')]!='' and Limp_df.loc[(n,'Ln (dBA) imp ')]!='':
            if Limp_df.loc[(n,'Ln (dBA) imp ')]-Ln.loc[(n,'Ln*')]<3:
                kin.append(0)
            elif Limp_df.loc[(n,'Ln (dBA) imp ')]-Ln.loc[(n,'Ln*')]<6:
                kin.append(3)
            else:
                kin.append(6)
        else:
            kin.append('')
            
    kid_df = pd.DataFrame(kid, index =[fecha_d],columns =['KI Ld'])
    kin_df =pd.DataFrame(kin, index =[fecha_n],columns =['KI Ln'])
    ki_df=pd.concat([kid_df,kin_df],axis=1)
    return(ki_df,kid,kin)
    
    
##############################################################################
##############################################################################

def Recibir_datos(rutPico,rutimp,rutLdLn,rutTerOct,estacion):
    output_final = pd.DataFrame()
    Lmax=Recibir_Lmax(rutPico) 
    L_imp=Recibir_impulso(rutimp)  
    (Ld,Ln)=Recibir_Ld_Ln(rutLdLn)
    (tonos_df,corre_df)=Recibir_corr_dia(rutTerOct)
    
    Ln.reset_index(drop=True, inplace=True)
    Ld.reset_index(drop=True, inplace=True)
    L_imp.reset_index(drop=True, inplace=True)
    Lmax.reset_index(drop=True, inplace=True)
    print('se cargo exitosamente '+ estacion)
    output_final= pd.concat([Ld,Ln,L_imp,Lmax], axis=1)
    return output_final 

###############################################################################
###############################################################################

"""CREACION DE TABLAS FINALES POR ESTACION"""

def Creartablafinal(rutPico,rutimp,rutLdLn,rutTerOct,estacion):
    """RECIBIR CORRECCIONES DE TERCIO DE OCTAVA"""
    (kt_d,kt_n,penal_df)=Recibir_corr_dia(rutTerOct)
    """RECIBIR NIVELES LD LN"""
    (Ld,Ln)=Recibir_Ld_Ln(rutLdLn)
    Ln.reset_index(drop=True, inplace=True)
    Ld.reset_index(drop=True, inplace=True)
    """RECIBIR NIVELES LMAX"""
    Lmax_df=Recibir_Lmax(rutPico)
    Lmax_df.reset_index(drop=True, inplace=True) 
    """RECIBIR NIVELES L Impulso"""
    Limp_df=Recibir_impulso(rutimp)
    Limp_df.reset_index(drop=True, inplace=True)
    """RECIBIR CORRECCIONES POR IMPULSIBIDAD (KI)"""
    (ki_df,kid,kin)=Recibir_ki(Ld, Ln, Limp_df)

    Ld_sincorr = []; Ln_sincorr = []; Lmax_d=[]; Lmax_n=[]; L90_d=[]; L90_n=[]
    L10_d=[]; L10_n=[]; SEL_d=[]; SEL_n=[]; Ld_imp =[]; Ln_imp =[]; ldn=[]
    Ld_corr=[]; Ln_corr=[]; Lpeak=[]; fechas=[]
    for i in range(len(Ld)):
        Ld_sincorr.append(Ld.loc[(i,'Ld*')])
        Ln_sincorr.append(Ln.loc[(i,'Ln*')])
        Lmax_d.append(Ld.loc[(i,'Lmax Ld')])
        Lmax_n.append(Ln.loc[(i,'Lmax Ln')])
        L90_d.append(Ld.loc[(i,'L90 Ld')])
        L90_n.append(Ln.loc[(i,'L90 Ln')])
        L10_d.append(Ld.loc[(i,'L10 Ld')])
        L10_n.append(Ln.loc[(i,'L10 Ln')])
        SEL_d.append(Ld.loc[(i,'SEL Ld')])
        SEL_n.append(Ln.loc[(i,'SEL Ln')])
    for i in range(len(Limp_df)):
        Ld_imp.append(Limp_df.loc[(i,'Ld (dBA) imp ')])
        Ln_imp.append(Limp_df.loc[(i,'Ln (dBA) imp ')])
    for i in range(len(Lmax_df)):
        Lpeak.append(Lmax_df.loc[(i,'Lmax (dBA)')])  
    for i in range(0,length_hint(Ln)):
        fechas.append(Ld.loc[(i,'Fecha')])
        
    """REALIZAR CORRECCIONES TONALES E IMPULSIVAS""" 
    for i in range(len(Ld_sincorr)):
        if Ld_sincorr[i]!='' and kt_d[i]!='' and kid[i]!='':
            Ld_corr.append(Ld_sincorr[i]+max(kt_d[i],kid[i]))
        else:
            Ld_corr.append('')
        if Ln_sincorr[i]!='' and kt_n[i]!='' and kin[i]!='':
            Ln_corr.append(Ln_sincorr[i]+max(kt_n[i],kin[i]))
        else:
            Ln_corr.append('')

    """CALCULO DE LDN"""
    for i in range(len(Ld_corr)):
        if Ld_corr[i]!='' and Ln_corr[i]!='':
            x1=((14*(10**(Ld_corr[i]/10)))+(10*(10**((Ln_corr[i]+10)/10))))/24
            Ldn=round(10*math.log10(x1),2)
            ldn.append(Ldn)
        else:
            ldn.append('')

    tabla_final = pd.DataFrame(index =[fechas],
                               columns =(['FECHA','Ld*','Ldimp','KId','KTd',
                                                              'LD','Ldmax','Ld90','Ld10','SEL D',
                                                              'Ln*','Lnimp','KIn','KTn','LN',
                                                              'Lnmax','Ln90','Ln10','SEL N','LDN',
                                                              'LPEAK',estacion,'','','','']))

    for i in range(len(Ld)):
        tabla_final.loc[(fechas[i],'FECHA')] = fechas[i]
        tabla_final.loc[(fechas[i],'Ld*')] = Ld_sincorr[i]
        tabla_final.loc[(fechas[i],'Ldimp')] = Ld_imp[i]
        tabla_final.loc[(fechas[i],'KId')] = kid[i]
        tabla_final.loc[(fechas[i],'LD')] = Ld_corr[i]
        tabla_final.loc[(fechas[i],'Ldmax')] = Lmax_d[i]
        tabla_final.loc[(fechas[i],'Ld90')] = L90_d[i]
        tabla_final.loc[(fechas[i],'Ld10')] = L10_d[i]
        tabla_final.loc[(fechas[i],'SEL D')] = SEL_d[i]
        tabla_final.loc[(fechas[i],'Ln*')] = Ln_sincorr[i]
        tabla_final.loc[(fechas[i],'Lnimp')] = Ln_imp[i]
        tabla_final.loc[(fechas[i],'KIn')] = kin[i]
        tabla_final.loc[(fechas[i],'LN')] = Ln_corr[i]
        tabla_final.loc[(fechas[i],'Lnmax')] = Lmax_n[i]
        tabla_final.loc[(fechas[i],'Ln90')] = L90_n[i]
        tabla_final.loc[(fechas[i],'Ln10')] = L10_n[i]
        tabla_final.loc[(fechas[i],'SEL N')] = SEL_n[i]
        tabla_final.loc[(fechas[i],'LDN')] = ldn[i]
        tabla_final.loc[(fechas[i],'KTd')] = kt_d[i]
        tabla_final.loc[(fechas[i],'KTn')] = kt_n[i]
        
        try:
            tabla_final.loc[(fechas[i],'LPEAK')] = Lpeak[i]
        except IndexError:
            tabla_final.loc[(fechas[i],'LPEAK')] = '' 
            break
    print('Carga de datos exitosa estacion '+ estacion)
    return(tabla_final)
    
###############################################################################
###############################################################################
    
""" CREACION DE DIRECCIONES PARA OBTENER DATOS DE CADA ESTACION"""

estaciones=['EMRI1','EMRI2','EMRI3','EMRI4','EMRI5','EMRI7','EMRI8','EMRI10',
            'EMRI11','EMRI13','EMRI15','EMRI17','EMRI18','EMRI19','EMRI20',
            'EMRI21','EMRI23','EMRI24','EMRI25','EMRI27','EMRI28','EMRI29',
            'EMRI30','EMRI32','EMRI33','EMRI34',]

d=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
             [],[],[],[],[],[]]

for i in range(len(estaciones)):
    rutLdLn=(r""+ estaciones[i] +"\\USERPER.000")
    rutPico=(r""+ estaciones[i] +"\\LEVELPER.000")
    rutimp=(r""+ estaciones[i] +"\\USERPER.001")
    rutTerOct=(r""+ estaciones[i] +"\\USERPER.001")
    d[i].append(rutPico)  
    d[i].append(rutimp)
    d[i].append(rutLdLn)
    d[i].append(rutTerOct)

###############################################################################
###############################################################################

""" CREACION TABLAS FINALES POR ESTACION"""

""" si alguna estacion no tiene datos para ese mes toca escribir lo siguiente:
    
    emri_3=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+2
    #emri_4=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
    EMRIS = pd.concat([emri_1, emri_2,emri_3,emri_5,emri_7,emri_8,emri_10,
                       emri_11,emri_13,emri_15,emri_17,emri_18,emri_19,emri_20,
                       emri_21,emri_23,emri_24,emri_25,emri_27,emri_28,emri_29,
                       emri_30,emri_32,emri_33,emri_34], axis=1)
    #emri_4.to_excel(writer,sheet_name='EMRI4')
    
    en este ejemplo la estacion que no tiene datos fue emri 4 """
        
u=0
emri_1=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_2=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_3=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_4=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_5=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_7=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_8=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_10=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_11=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_13=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_15=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_17=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_18=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_19=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_20=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_21=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_23=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_24=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_25=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_27=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_28=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_29=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_30=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_32=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_33=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1
emri_34=Creartablafinal(d[u][0],d[u][1],d[u][2],d[u][3],estaciones[u]);u=u+1


EMRIS = pd.concat([emri_1,emri_2,emri_3,emri_4,emri_5,emri_7,emri_8,emri_10,
                   emri_11,emri_13,emri_15,emri_17,emri_18,emri_19,emri_20,
                   emri_21,emri_23,emri_24,emri_25,emri_27,emri_28,emri_29,
                   emri_30,emri_32,emri_33,emri_34], axis=1)


###############################################################################
###############################################################################

""" EXPORTACION A EXCEL """

direccion=('Ruido_Estaciones.xlsx')

with pd.ExcelWriter(direccion, engine='xlsxwriter') as writer:
    EMRIS.to_excel(writer,sheet_name='EMRIS')
    emri_1.to_excel(writer,sheet_name='EMRI1')
    emri_2.to_excel(writer,sheet_name='EMRI2')
    emri_3.to_excel(writer,sheet_name='EMRI3')
    emri_4.to_excel(writer,sheet_name='EMRI4')
    emri_5.to_excel(writer,sheet_name='EMRI5')
    emri_7.to_excel(writer,sheet_name='EMRI7')
    emri_8.to_excel(writer,sheet_name='EMRI8')
    emri_10.to_excel(writer,sheet_name='EMRI10')
    emri_11.to_excel(writer,sheet_name='EMRI11')
    emri_13.to_excel(writer,sheet_name='EMRI13')
    emri_15.to_excel(writer,sheet_name='EMRI15')
    emri_17.to_excel(writer,sheet_name='EMRI17')
    emri_18.to_excel(writer,sheet_name='EMRI18')
    emri_19.to_excel(writer,sheet_name='EMRI19')
    emri_20.to_excel(writer,sheet_name='EMRI20')
    emri_21.to_excel(writer,sheet_name='EMRI21')
    emri_23.to_excel(writer,sheet_name='EMRI23')
    emri_24.to_excel(writer,sheet_name='EMRI24')
    emri_25.to_excel(writer,sheet_name='EMRI25')
    emri_27.to_excel(writer,sheet_name='EMRI27')
    emri_28.to_excel(writer,sheet_name='EMRI28')
    emri_29.to_excel(writer,sheet_name='EMRI29')
    emri_30.to_excel(writer,sheet_name='EMRI30')
    emri_32.to_excel(writer,sheet_name='EMRI32')
    emri_33.to_excel(writer,sheet_name='EMRI33')
    emri_34.to_excel(writer,sheet_name='EMRI34')
    
    
