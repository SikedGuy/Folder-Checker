## un-comment for CLI interface
#from Checker import Checker
#checkerNoGUI = Checker()
#checkerNoGUI.StartSearchNoGUI()
#exit(0)

from CheckerGUI import CheckerWithGUI

checker = CheckerWithGUI()
checker.Start()
