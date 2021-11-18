# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:56:22 2021

@author: klkel
"""

def conv2(f,w,pad):
    #project
    
    import cv2
    import numpy as np
    
    # f='lena.png' #img name
    # w=np.array([[-1, 1, -1],[-1, 1, -1],[-1, 1, -1]]) #kernel
    # w=np.array([[1,-1]]) #kernel
    
    # pad='cpEdge' #padding types
    
    
    img=cv2.imread(f)
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=gray.copy()
    
    w=np.array(w)
    
    pad_types={0:'blk',1:'wrap',2:'reflect',3:'cpEdge'}
    pad=pad_types[pad]
    
    # print(w.shape)
    if len(w.shape)==2:
        height_kernel,width_kernel=w.shape
    else:
        height_kernel=len(w)
        if height_kernel==1:
            width_kernel=w.shape
        else:
            width_kernel=0
    # print(len(w),height_kernel,width_kernel)
    # print(height_kernel,width_kernel)
    k_up=0  #kernel up
    k_down=0 #kernel down
    if height_kernel==0 or type(height_kernel)==tuple:
        k_up=0
        k_down=0
    elif height_kernel%2==0:
        #height even
        # print('even')
        up_dn=np.floor(height_kernel/2)
        k_up=up_dn
        k_down=-up_dn
    elif height_kernel==1:
        k_up=0
        k_down=0
    else:
        up_dn=np.floor(height_kernel/2)
        k_up=up_dn
        k_down=-up_dn
    # print('height, width',height_kernel,width_kernel)
    if width_kernel==0 or type(width_kernel)==tuple:
        #width 0
        k_lf=0
        k_rt=0
    elif width_kernel%2==0:
        #width even
        sides=np.floor(width_kernel/2)
        k_lf=-sides
        k_rt=sides
    elif width_kernel==1:
        k_lf=0
        k_rt=1
    else:
        sides=np.floor(width_kernel/2)
        k_lf=-sides
        k_rt=sides
    
    # print(k_down,k_up, k_lf,k_rt)
    hold=0
    w_val_x=0
    
    tot_sum=0 #
    for k in range(len(w)):
        if len(w.shape)==2 and w.shape[1]!=None:
            for l in range(len(w[k])):
                tot_sum=tot_sum+w[k][l]
        else:
            tot_sum=tot_sum+w[k]
    # print('tot',tot_sum)
    if tot_sum==0:
        tot_sum=1
    
    
        
        
    # print(k_down,k_up, k_lf,k_rt)
    
    if len(img.shape)==2:
        # print("Image is grey")
        img_type='gray'
        padding=np.zeros([img.shape[0]+2*height_kernel,img.shape[1]+2*width_kernel],dtype=np.uint8)
        height,width=img.shape
    if len(img.shape)==3:
        # print("Image is rgb")
        img_type='rgb'
        padding=np.zeros([img.shape[0]+2*height_kernel,img.shape[1]+2*width_kernel,img.shape[2]],dtype=np.uint8)
    
    #add img on black space (zero-padding for img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img_type=='gray':
                padding[i+height_kernel][j+width_kernel]=img[i][j] #get img to be centered
            else:
                for k in range(len(img[i][j])):
                    #print("hi")
                    padding[i+height_kernel][j+width_kernel][k]=img[i][j][k] #get img to be centered
       
    #top/bot
    for i in range(0,height_kernel):
        for j in range(0,len(img[i])):
            if pad=='wrap':
                #for wrap-around
                padding[height_kernel-i-1][j+width_kernel]=img[len(img)-1-i][j]
                padding[len(padding)-1-i][j+width_kernel]=img[height_kernel-i][j]
            if pad=='reflect':
                #for reflect
                padding[i][j+width_kernel]=img[height_kernel-i][j]
                padding[len(padding)-1-i][j+width_kernel]=img[len(img)-1-height_kernel+i][j]
                
            if pad=='cpEdge':
                padding[i][j+width_kernel]=img[0][j]
                padding[len(padding)-1-i][j+width_kernel]=img[len(img)-1][j]
                
    #sides lf/rt
    for i in range(0,len(img)):
        for j in range(width_kernel):        
            if pad=='wrap':
                #wrap
                padding[height_kernel+i][width_kernel-j-1]=img[i][len(img[height_kernel-i])-1-j] #left
                padding[i+height_kernel][len(padding[i+height_kernel])-width_kernel+j]=img[i][j] #right
                
            if pad=='reflect':
                #reflect
                padding[height_kernel+i][width_kernel-j-1]=img[i][j] #left
                padding[i+height_kernel][len(padding[i+height_kernel])-width_kernel+j]=img[i][len(img[height_kernel-i])-1-j] #right
                
            if pad=='cpEdge':
                #copy edge
                padding[height_kernel+i][j]=img[i][0]
                padding[i+height_kernel][len(padding[i+height_kernel])-width_kernel+j]=img[i][len(img[len(img)-1])-1]

    
    
    #edge
    for i in range(0,height_kernel):
        for j in range(0,width_kernel):
            if pad=='wrap':
                #wrap
                padding[i][j]=img[len(img)-1-height_kernel+i][len(img[len(img)-1-height_kernel+i])-1-width_kernel+j] #top left
                
                padding[len(padding)-1-i][j]=img[height_kernel-i][len(img[i])-1-width_kernel+j] #bot left
                
                padding[i][len(padding[i])-width_kernel+j]=img[len(img)-1-height_kernel+i][j] #top right
                
                padding[len(padding)-height_kernel+i][len(padding[i])-height_kernel+j]=img[i][j] #bot right
                
            if pad=='reflect':
                padding[i][j]=img[height_kernel-i][width_kernel-j] #top left
        
                padding[len(padding)-1-i][j] = img[len(img)-1-height_kernel+i][width_kernel-j] #bot left
                
                padding[i][len(padding[i])-width_kernel+j]=img[height_kernel-i][len(img[i])-1-j] #top right
                
                padding[len(padding)-height_kernel+i][len(padding[i])-height_kernel+j]=img[len(img)-1-i][len(img[len(img)-1-i])-1-j] #bot right
                
            if pad=='cpEdge':
                #copy edge
                padding[i][j]=img[0][0] #top left
                padding[len(padding)-1-i][j]=img[len(img)-1][0] #bot left
                
                padding[i][len(padding[i])-width_kernel+j]=img[0][len(img[0])-1] #top right
                
                padding[len(padding)-height_kernel+i][len(padding[i])-height_kernel+j]=img[len(img)-1][len(img[len(img)-1])-1] #bot right
        
    
    
    
    output_img=padding.copy()
    # print(len(output_img),len(output_img[0]))
    # print(len(padding),len(padding[0]))
    
    if img_type=='gray':
        for i in range(0,len(padding)-1):
            for j in range(0,len(padding[i])-1):
                val=0
                hold=0
                w_val_x=0
                if len(w.shape)==2 and w.shape[1]>1 and w.shape[0]>1: #kernel size is >=2x2
                    # print('here')
                    for k in range(int(k_down),int(k_up)):
                        
                        w_val_y=0
                        for l in range(int(k_lf),int(k_rt)):
                            
                            if i+k>=len(padding) or j+l>=len(padding[i]) or i+k<0 or j+l<0:
                                val=val
                            else:
                                val=val+(int(padding[i+k][j+l])*int(w[w_val_x][w_val_y]))
                                
                            w_val_y+=1
                        w_val_x+=1
                elif height_kernel>1 and width_kernel==1:
                    w_val_x=0
                    # print('turn',k_down,k_up)
                    
                    for k in range(int(k_down),int(k_up)):
                        # print('loop')
                        if i+k>=len(padding) or i+k<0:
                                val=val
                        else:
                            
                            # print('k,i-k',k,(i+k))
                            # print('pad',padding[i+k][j])
                            # print('w',w[w_val_x])
                            val=val+(int(padding[i+k][j])*int(w[w_val_x]))
                            
                        w_val_x+=1
                        # print('val:',val)
                elif height_kernel==1 and width_kernel>1:
                    w_val_x=0
                    for k in range(int(k_lf),int(k_rt)):
                        
                        if j+k>=len(padding[i]) or j+k<0:
                                val=val
                        else:
                            # print(padding[i][j+k])
                            # print(w[0][w_val_x])
                            val=val+(int(padding[i][j+k])*int(w[0][w_val_x]))
                            
                        w_val_x+=1
                        # print('val:',val,w_val_x)
                else:
                    # print('else')
                    for l in range(int(k_lf),int(k_rt)+1):
                        if j+l>=len(padding[i]) or i<0 or j+l<0:
                                val=val
                        else:
                            val=val+(int(padding[i][j+l])*int(w[w_val_x]))
                        w_val_x+=1
                        
                        # print('val:',val)
                hold=round(val/tot_sum)
                # print('hold',hold)
                if hold>255:
                    hold=255
                if hold<0:
                    hold=0
                    
                output_img[i][j]=hold    
    
                    
                val=0
            #     print(output_img[i][j])
                
            #     break
            # break
    else:
        print(w)
        for i in range(0,len(padding)):
            for j in range(0,len(padding)):
                
                for m in range(3): #colors
                    val=0
                    w_val_x=0
                    if len(w.shape)==2 and w.shape[1]>1 and w.shape[0]>1: #kernel size is >=2x2
                        # print('here')
                        for k in range(int(k_down),int(k_up)):
                            
                            w_val_y=0
                            for l in range(int(k_lf),int(k_rt)):
                                
                                if i+k>=len(padding) or j+l>=len(padding[i]) or i+k<0 or j+l<0 or w_val_x>len(w) or w_val_y>len(w[0]):
                                    val=val
                                else:
                                    val=val+(int(padding[i+k][j+l][m])*int(w[w_val_x][w_val_y]))
                                    
                                w_val_y+=1
                            w_val_x+=1
                    elif height_kernel>1 and width_kernel==1:
                        w_val_x=0
                        # print('turn',k_down,k_up)
                        
                        for k in range(int(k_down),int(k_up)):
                            # print('loop')
                            if i+k>=len(padding) or i+k<0  or j>=len(padding[i]) or w_val_x>=len(w):
                                    val=val
                            else:
                                
                                # print('k,i-k',k,(i+k))
                                # print('pad',padding[i+k][j])
                                # print('w',w[w_val_x])
                                val=val+(int(padding[i+k][j][m])*int(w[w_val_x]))
                                
                            w_val_x+=1
                            # print('val:',val)
                    elif height_kernel==1 and width_kernel>1:
                        w_val_x=0
                        for k in range(int(k_lf),int(k_rt)):
                            
                            if j+k>=len(padding[i]) or j+k<0:
                                    val=val
                            else:
                                # print(padding[i][j+k])
                                # print(w[0][w_val_x])
                                val=val+(int(padding[i][j+k][m])*int(w[0][w_val_x]))
                                
                            w_val_x+=1
                            # print('val:',val,w_val_x)
                    else:
                        # print('else')
                        for l in range(int(k_lf),int(k_rt)+1):
                            if j+l>=len(padding[i]) or i<0 or j+l<0:
                                    val=val
                            else:
                                val=val+(int(padding[i][j+l][m])*int(w[w_val_x]))
                            w_val_x+=1
                            
                            # print('val:',val)
                    hold=round(val/tot_sum)
                    # print('hold',hold)
                    if hold>255:
                        hold=255
                    if hold<0:
                        hold=0
                        
                    if i<len(output_img) and j<len(output_img[i]):
                        output_img[i][j][m]=hold 
    
    kernel=w/tot_sum
    dst=cv2.filter2D(padding,-1,kernel)    
    
    final_o=img.copy()
    shortened=img.copy()
    
    #crop version
    for i in range(0,len(img)):
        for j in range(0,len(img[i])):
            if img_type=='gray':
                final_o[i][j]=output_img[i+height_kernel][j+width_kernel]
                shortened[i][j]=dst[i+height_kernel][j+width_kernel]
            else:
                for m in range(0,len(img[i][j])):
                    final_o[i][j][m]=output_img[i+height_kernel][j+width_kernel][m]
                    shortened[i][j][m]=dst[i+height_kernel][j+width_kernel][m]
    
            
    # print(np.array_equal(shortened, final_o)) #How I tested 
        
    # cv2.namedWindow('original image',cv2.WINDOW_NORMAL)
    # cv2.imshow('original image',img)
    
    # pad_types={0:'blk',1:'wrap',2:'reflect',3:'cpEdge'}
    
    cv2.namedWindow('img w/ padding',cv2.WINDOW_NORMAL)
    cv2.imshow('img w/ padding',padding)
    
    cv2.imwrite("Grey BlackPadding.png",padding)
    cv2.namedWindow('output w/ padding',cv2.WINDOW_NORMAL)
    cv2.imshow('output w/ padding',output_img)
    
    # cv2.namedWindow('goal',cv2.WINDOW_NORMAL)
    # cv2.imshow('goal',shortened)
    cv2.namedWindow('output',cv2.WINDOW_NORMAL)
    cv2.imshow('output',final_o)
    
    cv2.imwrite("Grey BlackPadding Box Filter.png",final_o)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def DFT2(f):
    import cv2
    import numpy as np
    img=cv2.imread(f)
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=gray.copy()
    new_img=img.copy()
    fmin=img[0][0]
    fmax=img[0][0]
    
    #get max and min values
    for i in range(0,len(img)):
        for j in range(0,len(img[i])):
            if img[i][j]<fmin:
                fmin=img[i][j]
            if img[i][j]>fmax:
                fmax=img[i][j]
                
    #set values to be 0s or 1s
    for i in range(0,len(img)):
        for j in range(0,len(img[i])):
            new_img[i][j]=(round((img[i][j]-fmin)/(fmax-fmin))) #set img range 0-1
            
    #1->2d - fft
    
    fft_vals=np.fft.fft(new_img) #1d fft rows
    fft_val_t=np.transpose(fft_vals)
    fft_vals2=np.fft.fft(fft_val_t) #1d fft columns
    fft_output=np.transpose(fft_vals2)
    
    # Formula if I did not do fft function
    # for i in range(len(q1)): 
    #     fmu=np.asarray(q1[i],dtype=complex)
    #     M=fmu.shape[0]
    #     x=np.arange(M)
    #     mu=x.reshape((M,1))
    #     ep=np.exp(-2j*np.pi*mu*x/M)
    #     q2[i]=np.dot(ep,fmu)
    
    
    fft_compare=np.fft.fft2(new_img) #compare to function 2d-fft
    
    
    # print(np.array_equal(fft_output, fft_compare)) #is it a correct 1d to 2d fft?
    s=np.log(1+np.abs(fft_output))
    angle=s.copy()
    for i in range(0,len(fft_output)-1):
        s[i]=np.sqrt((fft_output[i].real**2)+(fft_output[i].imag**2)) #spectrum
        angle[i]=np.arctan(fft_output[i].imag/fft_output[i].real) #phase angle
        
        
    ifft_output=np.uint8(IDFT2(fft_output)) #inverse DFT2, still 0s and 1s
    
    

    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.namedWindow('spectrum',cv2.WINDOW_NORMAL)
    cv2.imshow('spectrum',s)
    cv2.namedWindow('phaseAngle',cv2.WINDOW_NORMAL)
    cv2.imshow('phaseAngle',angle)
    
    cv2.namedWindow('output',cv2.WINDOW_NORMAL)
    cv2.imshow('output',ifft_output)
    
    cv2.imwrite("Spectrum.png",s)
    
    cv2.imwrite("PhaseAngle.png",angle)
    
    cv2.imwrite("IFFT.png",ifft_output)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def IDFT2(fft_output):
    import cv2
    import numpy as np
    #2d-ifft:
    q1=np.fft.ifft(fft_output) #rows
    q1_t=np.transpose(q1)
    q2=np.fft.ifft(q1_t) #columns
    ifft_output=np.transpose(q2)
    
    # Formula if I did not do ifft function
    # for i in range(len(q1)): 
    #     fmu=np.asarray(q1[i],dtype=complex)
    #     M=fmu.shape[0]
    #     x=np.arange(M)
    #     mu=x.reshape((M,1))
    #     ep=np.exp(2j*np.pi*mu*x/M)
    #     q2[i]=np.dot(ep,fmu)/M
    
    
    for i in range(0,len(ifft_output)):
        for j in range(0,len(ifft_output[i])):
            ifft_output[i][j]=round(ifft_output[i][j].real) #get rid of imaginary and round real value
            
            
    
    return ifft_output
