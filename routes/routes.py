# Retic
from retic import Router

# Controllers
import controllers.mobi as mobi

"""Define router instance"""
router = Router()

"""Define all paths - build"""
router.post("/build/from-epub", mobi.build_mobi_from_epub_list)