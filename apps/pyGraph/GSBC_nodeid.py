def nodeid(cmaps):
    splug_14F = ['8347', '8348', '8349', '8350', '8351', '8419', '8514']
    CO2_14F = ['31401', '31402', '31403', '31404', '31405', '31406', '31407', '31408', '31409', '31410', '8549']
    splug_13F = ['8411', '8412', '8413', '8415', '8417', '8418', '8420', '8513']
    CO2_13F  = ['31301', '31302', '31303', '31305', '31306', '8539']
    splug_12F = ['8406', '8407', '8408', '8512']
    CO2_12F = ['31201', '31202', '31203', '31205', '31206', '31209', '31210', '8529']
    splug_11F = ['8339', '8340', '8345', '8346', '8401', '8402', '8403', '8404', '8405', '8549']
    CO2_11F = ['31101', '31102', '31103', '31104', '31105', '31106', '8511']
    splug_10F = ['8330', '8332', '8333', '8334', '8335', '8336', '8510']
    CO2_10F = ['31001', '31002', '31004', '31005', '31006', '31007', '31008', '8519']
    splug_9F = ['8324', '8329', '8331', '8509']
    CO2_9F = ['30901', '30902', '30903', '30904', '30905', '30906', '8590']
    splug_8F = ['8320', '8321', '8322', '8323', '8508']
    CO2_8F = ['30801', '30802', '30803', '30804', '30805', '30809', '8590']
    splug_7F = ['8310', '8311', '8312', '8314', '8315', '8316', '8341', '8342', '8507']
    CO2_7F = ['30701', '30702', '30704', '30705', '30706', '30707', '30709', '8570']
    splug_4F =['8306', '8307', '8308', '8309', '8504']
    CO2_4F = ['30401','30402', '30403', '30404', '30405', '30406', '30407', '30408', '8540']
    splug_3F = ['8301', '8302', '8303', '8304', '8503']
    CO2_3F = ['30302', '30303', '30304', '30307', '30308', '30309', '8530']
    hallCO2_2F = ['17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '0']
    hallCO2_1F = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '0']
    
    cmaps_14F = [('SPLUG 14F', splug_14F ), ('CO2 14F', CO2_14F)]
    cmaps_13F = [('SPLUG 13F', splug_13F ), ('CO2 13F', CO2_13F)]
    cmaps_12F = [('SPLUG 12F', splug_12F ), ('CO2 12F', CO2_12F)]
    cmaps_11F = [('SPLUG 11F', splug_11F ), ('CO2 11F', CO2_11F)]
    cmaps_10F = [('SPLUG 10F', splug_10F ), ('CO2 10F', CO2_10F)]
    cmaps_9F = [('SPLUG 9F', splug_9F ), ('CO2 9F', CO2_9F)]
    cmaps_8F = [('SPLUG 8F', splug_8F ), ('CO2 8F', CO2_8F)]
    cmaps_7F = [('SPLUG 7F', splug_7F ), ('CO2 7F', CO2_7F)]
    cmaps_4F = [('SPLUG 4F', splug_4F ), ('CO2 4F', CO2_4F)]
    cmaps_3F = [('SPLUG 3F', splug_3F ), ('CO2 3F', CO2_3F)]
    cmaps_2F = [('CO2 2F', hallCO2_2F)]
    cmaps_1F = [('CO2 1F', hallCO2_1F)]
    
    if cmaps==1 :
        return cmaps_1F
    elif cmaps==2 :
        return cmaps_2F
    elif cmaps==3 :
        return cmaps_3F
    elif cmaps==4 :
        return cmaps_4F
    elif cmaps==7 :
        return cmaps_7F
    elif cmaps==8 :
        return cmaps_8F
    elif cmaps==9 :
        return cmaps_9F
    elif cmaps==10 :
        return cmaps_10F
    elif cmaps==11 :
        return cmaps_11F
    elif cmaps==12 :
        return cmaps_12F
    elif cmaps==13 :
        return cmaps_13F
    elif cmaps==14 :
        return cmaps_14F
    else :
        return "error"