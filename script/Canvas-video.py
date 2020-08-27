
'''
Canvas Video V0.2 
converts a video file to a material and assigns it to plane.

Created by Matt Cromwell


'''


import c4d
from c4d import gui, storage
import os

def main():
    #load image from file loaction
    img = storage.LoadDialog() 
    if not img:
        return 'Canvas Cancelled.'
    else:
        path, filename = os.path.split(img)
        #get filename
        fname, ext = filename.split('.')

        #load movie
        if not ext in ('mp4','avi'):
            gui.MessageDialog('file format .' + ext +'  not supported!')
        else:
            mov = c4d.bitmaps.MovieLoader()
            mov.Open(img)

            frame, fps = mov.GetInfo()
            

            #create material
            mat = c4d.BaseMaterial(5703)   
            msg = gui.InputDialog('Material Name')
            mat[c4d.MATERIAL_USE_COLOR] = False
            mat[c4d.MATERIAL_USE_LUMINANCE] = True
            mat[c4d.MATERIAL_USE_REFLECTION] = False
            mat[c4d.MATERIAL_PREVIEWSIZE] = + 12
            mat[c4d.MATERIAL_ANIMATEPREVIEW] = True
            doc.StartUndo()
            doc.InsertMaterial(mat)    


            #create shader & add movie file
            mov_texture = c4d.BaseList2D(c4d.Xbitmap)    
            mov_texture[c4d.BITMAPSHADER_FILENAME] = img
            mov_texture[c4d.BITMAPSHADER_TIMING_TO] = frame
            mov_texture[c4d.BITMAPSHADER_TIMING_FPS] = fps     
            mat[c4d.MATERIAL_LUMINANCE_SHADER]= mov_texture        
            mat.InsertShader(mov_texture)
            
            #load bitmap from movie
            bm = c4d.bitmaps.BaseBitmap()
            bm.InitWith(img)
            getsize = bm.GetSize()
            x = getsize[0]
            y = getsize[1]
            
            alphaCheck = bm.GetChannelCount()

            # check if image has alpha channel
            if alphaCheck > 0:
                # Create alpha shader
                alpha_texture = c4d.BaseList2D(c4d.Xbitmap) 
                alpha_texture[c4d.BITMAPSHADER_FILENAME] = img  
                mat[c4d.MATERIAL_USE_ALPHA] = True    
                mat[c4d.MATERIAL_ALPHA_SHADER]= alpha_texture        
                mat.InsertShader(alpha_texture)
                doc.AddUndo(c4d.UNDOTYPE_NEW, alpha_texture)
            else:
                pass

            # create plane
            plane = c4d.BaseObject(5168)
            plane[c4d.PRIM_PLANE_SUBW] = 1
            plane[c4d.PRIM_PLANE_SUBH] = 1
            plane[c4d.PRIM_PLANE_WIDTH] = x
            plane[c4d.PRIM_PLANE_HEIGHT] = y
            doc.InsertObject(plane)
            # assign texture tag to plane
            tag = plane.MakeTag(c4d.Ttexture)
            tag[c4d.TEXTURETAG_PROJECTION] = 6
            tag[c4d.TEXTURETAG_MATERIAL]= mat
            
            # edit name
            if msg in(None,'Material Name?'):
                mat[c4d.ID_BASELIST_NAME] = fname
                plane[c4d.ID_BASELIST_NAME] = fname
            else:
                mat[c4d.ID_BASELIST_NAME] = msg
                plane[c4d.ID_BASELIST_NAME] = msg
            
            # update undos
            doc.AddUndo(c4d.UNDOTYPE_NEW, plane)
            doc.AddUndo(c4d.UNDOTYPE_NEW, mat)
            doc.AddUndo(c4d.UNDOTYPE_NEW, mov_texture)
            doc.EndUndo()
            # add to file
            c4d.EventAdd()

if __name__=='__main__':
    main()
