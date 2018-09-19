from bsite.models import Project, ProjectUser, Wallet

def UserProfileTransactions(request):

    try:
        userWallet = Wallet.objects.get(idUser = request.user.id)
        userProjectsIds = ProjectUser.objects.filter(idUser = request.user.id)

        for userProjectId in userProjectsIds:
            project = Project.objects.get(idProject = userProjectId.idProject)
            ownerWallet = Wallet.objects.get(idUser = project.projectOwner)

            #transacciones = funcionDeYonyKrac(userWallet.address, ownerWallet.address)
            
    except expression as identifier:
        pass

