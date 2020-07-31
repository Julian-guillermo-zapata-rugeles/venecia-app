__Author__="Julian Guillermo Zapata Rugeles"

contenido="""
              <div class="card p-3 mt-2">
                  <div class="d-flex justify-content-between align-items-center">
                      <div class="user d-flex flex-row align-items-center"> <img src="log.png" width="30" class="user-img rounded-circle mr-2"> <span><small class="font-weight-bold text-primary"></small> NAME <small class="font-weight-bold text-primary"></small> <br> <small class="font-weight-bold text-primary">TELEFONO: </small> <small class="font-weight-bold">TELEPHONE</small></span> </div> <small>Julio(2020)</small>
                  </div>
                  <div class="action d-flex justify-content-between mt-2 align-items-center">
                      <div class="reply px-4"> <span class="dots"></span> <small></small> </div>
                      <div class="icons align-items-center"> <i class="fa fa-check-circle-o check-icon text-primary"></i> </div>
                  </div>
              </div>
"""
header="""
<!DOCTYPE html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<html lang="en" dir="ltr">
<link rel="stylesheet" href="bootstrap.min.css">
<link rel="stylesheet" href="restaurante.css">
<body>
  <div class="container mt-5">
      <div class="row d-flex justify-content-center">
          <div class="col-md-8">
              <div class="headings d-flex justify-content-between align-items-center mb-3">
                  <h5>TITLE</h5>
                  <div class="buttons"> <span class="badge bg-white d-flex flex-row align-items-center"> <span class="text-primary"><a href="index.html">PERSONAS</a></span>
                      </span> </div>
              </div>


"""
header2="""
              <div class="card p-3 mt-2">
                  <div class="d-flex justify-content-between align-items-center">
                      <div class="user d-flex flex-row align-items-center"> <img src="litle.png" width="30" class="user-img rounded-circle mr-2"> <span><small class="font-weight-bold text-primary"></small> TITLE <small class="font-weight-bold text-primary"></small> <br> <small class="font-weight-bold text-primary">EXP</small> <small class="font-weight-bold"></small></span> </div> <small>Julio(2020)</small>
                  </div>
                  <div class="action d-flex justify-content-between mt-2 align-items-center">
                      <div class="reply px-4"> <span class="dots"></span> <small></small> </div>
                      BUTTON
                      <div class="icons align-items-center"> <i class="fa fa-check-circle-o check-icon text-primary"></i> </div>
                  </div>
              </div>
"""
class TemplateGenerator():
    """ generadora de plantillas html """
    def __init__(self,fileName):

        try:
            self.readFile=open(fileName).read().split("</end>")
        except Exception as e:
            print("Error al encontrar el archivo")
            exit()
    def tablas(self):
        index=open("index.html","w")
        index.write(header)
        for files in self.readFile:
            print(files)
            temList=files.split('\n')
            print(temList)
            counter=0
            for elements in temList:
                if elements!="":
                    if counter==0:
                        print(elements)
                        st=elements.replace(" ","")+".html"
                        button="""<button type='button' class='btn btn-success' onclick="window.location.href='{}'">Explorar</button>""".format(st)
                        print(button)
                        file=open(st,"w")
                        title=header
                        title2=header2
                        title=title.replace("TITLE",elements)
                        title2=title2.replace("TITLE",elements)
                        title2=title2.replace("BUTTON",button)
                        file.write(title)
                        index.write(title2)
                        counter=counter+1
                    else:
                        content=elements.split(';')
                        table=contenido
                        table=table.replace("NAME",content[0])
                        table=table.replace("TELEPHONE",content[1])
                        file.write(table)
                        counter=counter+1
            file.close()
        index.close()

TemplateGenerator("data.txt").tablas()
