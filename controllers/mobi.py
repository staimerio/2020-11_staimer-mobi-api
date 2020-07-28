# Retic
from retic import Request, Response, Next

# Services
import services.mobi.mobi as mobi
from retic.services.validations import validate_obligate_fields
from retic.services.responses import success_response_service, error_response_service


def build_mobi_from_epub_list(req: Request, res: Response, next: Next):
    """Build a mobi file from a epub file"""

    """Get the files from the request, if it doesn't exist,
    return an empty list"""
    _files = req.files.getlist('files') or list()

    """Validate obligate params"""
    _validate = validate_obligate_fields({
        u'files': _files,
    })

    """Check if has errors return a error response"""
    if _validate["valid"] is False:
        return res.bad_request(
            error_response_service(
                "The param {} is necesary.".format(_validate["error"])
            )
        )

    """Create file"""
    _file = mobi.build_from_epub_list(
        _files,
        req.param('binary_response'),
    )

    """Check if error exists"""
    if _file['valid'] is False:
        res.not_found(_file)

    """Transform data response"""
    _data_response = {
        u"files": _file['data'],
    }

    """Response to client"""
    res.ok(
        success_response_service(
            data=_data_response,
            msg="Files created."
        )
    )