import pickle
f=open("filep.txt","wb");
pickle.dump(10,f)
pickle.dump(20.5,f);
pickle.dump("hello",f);
pickle.dump(["xyz",7.5],f);
pickle.dump(('mango','banana'),f);
pickle.dump({'apple':10},f);
f.close();
