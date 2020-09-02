import c4d
from c4d import gui, storage
import os



def ImagePlane(mat,name,bmSize):
    ### create plane
    plane = c4d.BaseObject(5168)
    plane[c4d.PRIM_PLANE_SUBW] = 1
    plane[c4d.PRIM_PLANE_SUBH] = 1
    plane[c4d.PRIM_PLANE_WIDTH] = bmSize[0]
    plane[c4d.PRIM_PLANE_HEIGHT] = bmSize[1]
    doc.InsertObject(plane)
    ##assign texture tag to plane
    tag = plane.MakeTag(c4d.Ttexture)
    tag[c4d.TEXTURETAG_PROJECTION] = 6
    tag[c4d.TEXTURETAG_MATERIAL]= mat
    doc.AddUndo(c4d.UNDOTYPE_NEW, plane)
    return plane

def Material(img):
    #create material
    mat = c4d.BaseMaterial(5703)   
    mat[c4d.MATERIAL_USE_COLOR] = False
    mat[c4d.MATERIAL_USE_LUMINANCE] = True
    mat[c4d.MATERIAL_USE_ALPHA] = True
    mat[c4d.MATERIAL_USE_REFLECTION] = False
    mat[c4d.MATERIAL_PREVIEWSIZE] = + 12
    mat[c4d.MATERIAL_ANIMATEPREVIEW] = True
    doc.AddUndo(c4d.UNDOTYPE_NEW, mat)
    doc.InsertMaterial(mat)
    return mat 

def alphaCheck(mat,bm,img):
    
    alphaCheck = bm.GetChannelCount()
    ### check if image has alpha channel
    if alphaCheck > 0:
        ### Create alpha shader
        alpha_texture = c4d.BaseList2D(c4d.Xbitmap)    
        alpha_texture[c4d.BITMAPSHADER_FILENAME] = img   
        mat[c4d.MATERIAL_ALPHA_SHADER]= alpha_texture        
        mat.InsertShader(alpha_texture)
        doc.AddUndo(c4d.UNDOTYPE_NEW, alpha_texture)
    else:
        pass


def materialShader(mat,img):
    shdr_texture = c4d.BaseList2D(c4d.Xbitmap)   
    shdr_texture[c4d.BITMAPSHADER_FILENAME] = img    
    mat[c4d.MATERIAL_LUMINANCE_SHADER]= shdr_texture        
    mat.InsertShader(shdr_texture)
     #create bitmap
    bm = c4d.bitmaps.BaseBitmap()
    bm.InitWith(img)
    getsize = bm.GetSize()
    x = getsize[0]
    y = getsize[1]
    alphaCheck(mat,bm,img)
    bmSize = [x,y]
    doc.AddUndo(c4d.UNDOTYPE_NEW, shdr_texture)
    return bmSize


def CanvasSequence():
    img = storage.LoadDialog() 
    if not img:
        return 'Canvas Cancelled.'
    else:
        path, filename = os.path.split(img)
        #gets directory and lists all images - helps calculate total frames.
        imgSeq = os.listdir(path)
        #gets length of frames
        frames = len(imgSeq)
        #user input framerate
        fps = gui.InputDialog('Framerate')
        #get filename
        fname, ext = filename.split('.')

def CanvasVideo():
    pass

def CanvasImage():
     img = storage.LoadDialog() 
     if not img:
        return 'Canvas Cancelled.'
     else:
        path, filename = os.path.split(img)
        #get filename
        fname, ext = filename.split('.')
        name = gui.InputDialog('Material Name')
        m = Material(img)
        ms = materialShader(m,img)
        p = ImagePlane(m,name,ms)
        if name in(None,'Material Name?'):
            m[c4d.ID_BASELIST_NAME] = fname
            p[c4d.ID_BASELIST_NAME] = fname
           
        else:
            m[c4d.ID_BASELIST_NAME] = name
            p[c4d.ID_BASELIST_NAME] = name
    
    
    
   


class mainDialog(c4d.gui.GeDialog): 
    def CreateLayout(self):
        self.SetTitle('Canvas') 
        self.AddStaticText(102,c4d.BFH_CENTER,280,15,'Click on a Canvas type below',0)
        self.GroupBegin(id=0, flags=c4d.BFH_SCALEFIT, rows=1, title="", cols=3, groupflags=0)
        self.Imagebtn = self.AddButton(1003, c4d.BFH_CENTER, 60, 10, "Image") 
        self.Videobtn = self.AddButton(1004, c4d.BFH_CENTER, 60, 10, "Video") 
        self.Sequencebtn = self.AddButton(1005, c4d.BFH_CENTER, 120, 10, "Image Sequence") 
        self.Enable(1001,True)
        return True
    
    def Command(self,id,msg): #listen for user clicks
        c4d.StopAllThreads()
        if id==1004:
            print('video')
        elif id ==1003:
            doc.StartUndo()
            print('image')
            CanvasImage()
        else:
            print('image sequence')
        return True

    
def main():
    main_dlg = mainDialog() #instance mainDialog clas
    main_dlg.Open(dlgtype=c4d.DLG_TYPE_MODAL, defaultw=300, defaulth=100, xpos=-1, ypos=-1) #open main_dialog
    c4d.EventAdd()
if __name__=='__main__':
    main() # run