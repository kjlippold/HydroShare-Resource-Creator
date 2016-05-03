from tethys_sdk.base import TethysAppBase, url_map_maker


class HydroshareResourceCreator(TethysAppBase):
    """
    Tethys app class for HydroShare Resource Creator.
    """

    name = 'HydroShare Resource Creator'
    index = 'hydroshare_resource_creator:home'
    icon = 'hydroshare_resource_creator/images/icon.gif'
    package = 'hydroshare_resource_creator'
    root_url = 'hydroshare-resource-creator'
    color = '#2ecc71'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='hydroshare-resource-creator',
                           controller='hydroshare_resource_creator.controllers.home'),
                    UrlMap(name='chart_data',
                           url='chart_data/{res_id}/{src}',
                           controller='hydroshare_resource_creator.controllers.chart_data'),
        )

        return url_maps