import getOpenData

extension = ".csv"
url = "https://www.data.gouv.fr/fr/datasets/base-de-donnees-accidents-corporels-de-la-circulation/"
dossier = "data"


getOpenData.find_data(url, extension, dossier)