import SkuStorage

def AddProductNameToObject(finalResponse):
    newObject = []
    for i in finalResponse:
        passedOBJ = i[0]
        SKUGroup = passedOBJ.get('SKU Group').strip()
        SKU  = passedOBJ.get('SKU').strip()
        FinancialCode = passedOBJ.get('Financial Code').strip()
        GoodQuantityFloat = float(passedOBJ['Good Quantity'])
        if SKU in SkuStorage.ConeBodies6276_1:
            passedOBJ['Product'] = 'Cone Bodies'
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.DistalStem127StraightSkus:
            passedOBJ['Product'] = 'Distal Stem 127'
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.DistalStem167StraightSkus:
            passedOBJ['Product'] = "Distal Stem 167"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.SpineAL4801Skus:
            passedOBJ['Product'] = "Spine AL"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.SpineTL4893Skus:
            passedOBJ['Product'] = "Spine TL"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.TricSkus:
            passedOBJ['Product'] = "Tri C"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.PL1Skus:
            passedOBJ['Product'] = "PL1"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.PL1SampleSkus:
            passedOBJ['Product'] = "PL1 Sample"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.PL2Skus:
            passedOBJ['Product'] = "Pl2"
        elif SKU in SkuStorage.CrossfirePETrident621_10Skus:
            passedOBJ['Product'] = "Crossfire PE Trident"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.CrossfirePETrident621_05Skus:
            passedOBJ['Product'] = "Crossfire PE Trident"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.DallMiles3704_8Skus:
            passedOBJ['Product'] = "Dall Miles"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.DallMiles6704_8Skus:
            passedOBJ['Product'] = "Dall Miles"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.DallMiles6704_4Skus:
            passedOBJ['Product'] = "Dall Miles"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.DallMiles3704_1Skus:
            passedOBJ['Product'] = "Dall Miles"
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.ADMSkus:
            passedOBJ['Product'] = 'ADM'
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.TridentII3D709_04Skus:
            passedOBJ['Product'] = 'TridentII3D'
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.AccoladeII6721Skus:
            passedOBJ['Product'] = 'AccoladeII'
            newObject.append([passedOBJ])
        elif SKU in SkuStorage.AccoladeII6720Skus:
            passedOBJ['Product'] = 'AccoladeII'
            newObject.append([passedOBJ])
    return newObject
        
def AddStepNameToObject(ObjectWithProductName):
    finalObject = []
    for i in ObjectWithProductName:
        passedOBJ = i[0]
        Product = passedOBJ.get('Product')
        Step = passedOBJ.get('OP Sequence').strip()
        FinCode = passedOBJ.get('Financial Code').strip()
        if Step == '10':
            passedOBJ['Step'] = 'Assign To Floor'
            finalObject.append([passedOBJ])
        elif FinCode == 'Z06':
            passedOBJ['Step'] = 'Ship To Sterilization'
            finalObject.append([passedOBJ])
    return finalObject


