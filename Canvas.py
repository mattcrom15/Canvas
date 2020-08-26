import c4d
from c4d import gui, storage
import os


def main():
    #load image from file loaction
    img = storage.LoadDialog() 
    path, filename = os.path.split(img)
    #get filename
    fname, ext = filename.split('.')

    
 
   
    #create material
    mat = c4d.BaseMaterial(5703)    ##create material
    msg = gui.RenameDialog('Material Name?')
    mat[c4d.MATERIAL_USE_COLOR] = False
    mat[c4d.MATERIAL_USE_LUMINANCE] = True
    mat[c4d.MATERIAL_USE_ALPHA] = True
    mat[c4d.MATERIAL_USE_REFLECTION] = False
    mat[c4d.MATERIAL_PREVIEWSIZE] = + 12
    mat[c4d.MATERIAL_ANIMATEPREVIEW] = True
    doc.StartUndo()
    doc.InsertMaterial(mat)    ###Insert material into document
        
    shdr_texture = c4d.BaseList2D(c4d.Xbitmap)    ##create shader
    shdr_texture[c4d.BITMAPSHADER_FILENAME] = img    ##add image to shader 
    mat[c4d.MATERIAL_LUMINANCE_SHADER]= shdr_texture        
    mat.InsertShader(shdr_texture)
    
    
    bm = c4d.bitmaps.BaseBitmap()
    bm.InitWith(img)
    getsize = bm.GetSize()
    x = getsize[0]
    y = getsize[1]
    
    c = bm.GetChannelCount()
    print(c)
    
    if c > 0:
        alpha_texture = c4d.BaseList2D(c4d.Xbitmap)    ##create shader
        alpha_texture[c4d.BITMAPSHADER_FILENAME] = img    ##add image to shader 
        mat[c4d.MATERIAL_ALPHA_SHADER]= alpha_texture        
        mat.InsertShader(alpha_texture)
    else:
        pass

    
    plane = c4d.BaseObject(5168)
    plane[c4d.PRIM_PLANE_SUBW] = 1
    plane[c4d.PRIM_PLANE_SUBH] = 1
    plane[c4d.PRIM_PLANE_WIDTH] = x
    plane[c4d.PRIM_PLANE_HEIGHT] = y
    doc.InsertObject(plane)
    
    tag = plane.MakeTag(c4d.Ttexture)
    tag[c4d.TEXTURETAG_PROJECTION] = 6
    tag[c4d.TEXTURETAG_MATERIAL]= mat
    
    ## edit name
    if msg == None:
        mat[c4d.ID_BASELIST_NAME] = fname
        plane[c4d.ID_BASELIST_NAME] = fname
    else:
        mat[c4d.ID_BASELIST_NAME] = msg
        plane[c4d.ID_BASELIST_NAME] = msg
    
    ##update undos
    doc.AddUndo(c4d.UNDOTYPE_NEW, plane)
    doc.AddUndo(c4d.UNDOTYPE_NEW, mat)
    doc.AddUndo(c4d.UNDOTYPE_NEW, alpha_texture)
    doc.AddUndo(c4d.UNDOTYPE_NEW, shdr_texture)
    doc.EndUndo()
    ##add to file
    c4d.EventAdd()

if __name__=='__main__':
    main()
