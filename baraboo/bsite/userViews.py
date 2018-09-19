from bsite.models import Project, ProjectUser, Wallet
from bsite.walletTransactions import getTotalTransfersBetweeenWallets

def UserProfileTransactions(request):

    try:
        userWallet = Wallet.objects.get(idUser = request.user.id)
        userProjectsIds = ProjectUser.objects.filter(idUser = request.user.id)
        totalTrasaction = []

        for userProjectId in userProjectsIds:
            project = Project.objects.get(idProject = userProjectId.idProject)
            ownerWallet = Wallet.objects.get(idUser = project.projectOwner)

            transacciones = getTotalTransfersBetweeenWallets(ownerWallet.address, userWallet.address)
            totalTrasaction.append(transacciones)
            
    except expression as identifier:
        pass

