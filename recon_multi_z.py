\
    # recon_multi_z.py - multi-z hologram reconstructor with noise injection
    import numpy as np, argparse, imageio, os
    from numpy.fft import fft2, ifft2
    try:
        from skimage.restoration import unwrap_phase as sk_unwrap
        HAVE_SK = True
    except:
        HAVE_SK = False

    def read_img(fname):
        im = imageio.v2.imread(fname)
        if im.ndim==3:
            im = np.dot(im[...,:3], [0.2989,0.5870,0.1140])
        return im.astype(np.float64)/255.0

    def angular_spectrum(U0,w,z,dx):
        Ny,Nx=U0.shape
        k=2*np.pi/w
        fx=np.fft.fftfreq(Nx,dx); fy=np.fft.fftfreq(Ny,dx)
        FX,FY=np.meshgrid(fx,fy)
        H=np.exp(1j*k*z*np.sqrt(np.maximum(0,1-(w*FX)**2-(w*FY)**2)))
        return ifft2(fft2(U0)*H)

    def unwrap(p):
        if HAVE_SK:
            try: return sk_unwrap(p)
            except: pass
        return np.unwrap(np.unwrap(p,axis=1),axis=0)

    if __name__=="__main__":
        ap=argparse.ArgumentParser()
        ap.add_argument("holo")
        ap.add_argument("--zs",type=float,nargs="+",required=True)
        ap.add_argument("--wavelength",type=float,default=532e-9)
        ap.add_argument("--dx",type=float,default=6.5e-6)
        ap.add_argument("--outdir",default="multi_recon")
        ap.add_argument("--unwrap",action="store_true")
        ap.add_argument("--noise",type=float,default=0.0)
        args=ap.parse_args()
        os.makedirs(args.outdir,exist_ok=True)
        holo=read_img(args.holo)
        if args.noise>0:
            holo+=args.noise*np.random.randn(*holo.shape)
            holo=np.clip(holo,0,1)
        U=np.sqrt(holo)
        for z in args.zs:
            U1=angular_spectrum(U,args.wavelength,-z,args.dx)
            amp,phs=np.abs(U1),np.angle(U1)
            if args.unwrap: phs=unwrap(phs)
            import imageio
            imageio.v2.imwrite(os.path.join(args.outdir,f"amp_z{z*1000:.0f}mm.png"),
                (255*np.clip(amp/amp.max(),0,1)).astype('uint8'))
            pmin,pmax=phs.min(),phs.max()
            pn=(phs-pmin)/(pmax-pmin) if pmax>pmin else np.zeros_like(phs)
            imageio.v2.imwrite(os.path.join(args.outdir,f"phase_z{z*1000:.0f}mm.png"),
                (255*pn).astype('uint8'))
            print("Saved recon at z=%.3f m"%z)
