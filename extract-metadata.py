import openpyxl
import docx
import PyPDF2


#PARA .XLSX
def xlsx_meta(nombre):
    wb = openpyxl.load_workbook(nombre)
    metadata = {}

    
    props = wb.properties
    metadata['Titulo'] = props.title
    metadata['Creador'] = props.creator
    metadata['descripción'] = props.description
    metadata['Creación'] = props.created.isoformat() if props.created else None
    metadata['Modificado'] = props.modified.isoformat() if props.modified else None

    return metadata


#PARA .DOCX
def docx_meta(nombre):
    doc = docx.Document(nombre)
    metadata = {}

   
    core_properties = doc.core_properties
    metadata['Titulo'] = core_properties.title
    metadata['Autor'] = core_properties.author
    metadata['Creación'] = core_properties.created
    metadata['Modificado'] = core_properties.modified
    metadata['Última modificación'] = core_properties.last_modified_by
    metadata['Revision'] = core_properties.revision
    metadata['version'] = core_properties.version

    return metadata
    
    
#PARA .PDF
def pdf_meta(nombre):
    with open(nombre, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        metadata = {}
        info = pdf_reader.metadata
        for key in info:
            metadata[key] = info[key]
        return metadata

if __name__ == "__main__":

    # DATOS PARA PDF
    print("\n∞∞∞ Metadatos de PDF ∞∞∞")
    #RUTA PDF
    pdf_metadata = pdf_meta("/home/tabatha/metadatos/practica1.pdf")
    for key, value in pdf_metadata.items():
        print(f"{key}: {value}")
        
    # DATOS PARA DOCX
    print("\n∞∞∞ Metadatos de DOCX ∞∞∞")
    #RUTA DOC
    docx_metadata = docx_meta("/home/tabatha/metadatos/ejercicio1.docx")
    for key, value in docx_metadata.items():
        print(f"{key}: {value}")
        
    # DATOS PARA XLSX
    print("\n∞∞∞ Metadatos de XLSX ∞∞∞")
    #RUTA XLSX
    xlsx_metadata = xlsx_meta("/home/tabatha/metadatos/tabatha.xlsx")
    for key, value in xlsx_metadata.items():
        print(f"{key}: {value}")
